#Este archivo esta enfocado para linux actualmente
# y esta comentado con hibrido spanish / ingles
#Para windows, cambie touch por echo. >
# o por un comando similar
def char_catch(text:str)->list: #retorna los caracteres unicos de un texto
     a=[]
     for i in text:
         if not i in a:
             a.append(i)
     return a
def folder_order(text,
    ignore_chars:list[chr], #Caracteres, letras, o simbolos a ignorar
    intentSensibility:int=3, #sensibilidad por simbolo bloque, bloque=intentSymbol_quantity//intentSensibility
    intentSymbol:list[chr]=[' '], #simbolo de bloque de carpeta hija
    endSymbol:list[chr]=['\n','#','/']
    )->str: #Retorna conjunto de instrucciones para crear arboles.
    if(any(symbol in ignore_chars for symbol in intentSymbol)):
        raise Exception("Simbolo de separacion en ignorar")
    word="" #Palabra que acumula el nombre de la carpeta
    order="" #Los comandos de creacion de carpetas
    prevWord=""
    intentSymbol_quantity=0
    deepness=0 #nivel de carpeta hija
    skip=False #Automaticamente se pasara a la siguiente linea si 
    for i in range(len(text)):
        if(text[i] in ignore_chars):
            continue
        elif(skip==True):
            if(text[i]=='\n'):
                skip=False
                intentSymbol_quantity=0
            continue
        elif(text[i] in endSymbol or i==len(text)-1):
            if(word!=""):
                if(intentSymbol_quantity//intentSensibility>deepness):#Si es hija del ultimo padre
                    deepness=deepness+1 #Se ingresa profundidad
                    order=order+"\n"+"cd "+prevWord #Va a el padre
                elif(intentSymbol_quantity//intentSensibility<deepness):#Si no es hija del ultimo padre
                    deepness=deepness-1 #Se resta profundidad
                    order=order+"\n"+"cd ../" #Vuelve al padre del padre 
                if(word.find('.')!=-1 and word.find('/')==-1
                and text[i]!='/'):
                    order=order+"\n"+"touch "+word #Si es archivo, solo se crea
                else:
                    order = order+"\n"+"mkdir "+word
                    prevWord = word #Si es carpeta entonces se convierte en padre
                print(word)
                print(repr(text[i]))
                if(text[i]!='\n'):
                    skip=True
                print(skip)
                print(intentSymbol_quantity)
            if(i==len(text)-1 and deepness>0):
                for i in range(deepness):
                    order=order+"\n"+"cd ../"
            intentSymbol_quantity=0
            word=""
        elif(text[i] in intentSymbol):
            intentSymbol_quantity=intentSymbol_quantity+1
        else:
            word=word+text[i]
    return order
def execute(order:str): #Ejecuta la orden en el sistema
    import subprocess #Remplazo de la funcion os.system(order)
    from dotenv import load_dotenv
    load_dotenv()
    subprocess.run(order)

def loadTextFrom(file):
    file=open(file,'r')
    return file.read(-1)#retorna todo el texto
if __name__=="__main__":
    text=loadTextFrom("folderStr.txt")
    intentSymbol=[' ','─','└','├','│']
    special_allow_chars=['.','\n','/']
    ignore_chars=[char for char in char_catch(text)
                if char not in special_allow_chars
                and char.isalnum()==False 
                and char not in intentSymbol
                ]
    print("Los siguientes caracteres son ignorados:\n",ignore_chars)
    endsymbol=['\n','#','/','(']
    order=folder_order(
            text,
            ignore_chars,
            4,
            intentSymbol,
            endsymbol
        )
    end=False
    time=0
    while time<10:
        time=time+1
        print(order+"\nwill be executed, proceed?\nY/N")
        match input().lower():
            case 'y':
                execute(order)
                time=10
                print("order executed")
            case 'n':
                print("order cancelled")
                time=10
            case _:
                print("answer not valid")
                if(time==10):
                    print("automatic cancel activated.")
