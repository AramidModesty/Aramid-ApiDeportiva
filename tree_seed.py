def char_catch(text:str)->list:
     a=[]
     for i in text:
         if not i in a:
             a.append(i)
     return a
def folder_order(text,
    ignore_chars:list[chr], #Caracteres, letras, o simbolos a ignorar
    intentSensibility:int=3, #sensibilidad por simbolo bloque, bloque=intentSymbol_quantity//intentSensibility
    intentSymbol:list[chr]=[' '], #simbolo de bloque de carpeta hija
    endSymbol:list[chr]=['\n']
    )->str:
    if(any(symbol in ignore_chars for symbol in intentSymbol)):
        raise Exception("Simbolo de separacion en ignorar")
    word="" #Palabra que acumula el nombre de la carpeta
    order="" #Los comandos de creacion de carpetas
    prevWord=""
    intentSymbol_quantity=0
    deepness=0 #nivel de carpeta hija
    for i in range(len(text)):
        if(text[i] in ignore_chars):
            continue
        elif(text[i] in endSymbol or i==len(text)-1):
            assert word.isascii() or word=="" , f"Nombre de carpeta no valido:{word}"
            if(intentSymbol_quantity==0 and prevWord!=""):
                order=order+"\n"+"cd ../"
                deepness=deepness-1
            intentSymbol_quantity=0
            if(word!=""):
                order = order+"\n"+"mkdir "+word
                prevWord = word
            word=""
            if(i==len(text)-1 and deepness>0):
                for i in range(deepness):
                    order=order+"\n"+"cd ../"
        elif(text[i] in intentSymbol):
            intentSymbol_quantity=intentSymbol_quantity+1
            if(intentSymbol_quantity%intentSensibility==0 and prevWord!=""):
                if(intentSymbol_quantity//intentSensibility>deepness):
                    deepness=deepness+1
                    order=order+"\n"+"cd "+prevWord
                elif(intentSymbol_quantity//intentSensibility<deepness
                     and text[i+1] not in intentSymbol):
                    deepness=deepness-1
                    order=order+"\n"+"cd ../"
        else:
            word=word+text[i]
    return order
text="""
SportsLeague.Domain/
├── Entities/
├── Enums/
├── Interfaces/
│   ├── Repositories/
│   └── Services/
└── Services/
"""
if __name__=="__main__":
    intentSymbol=[' ','─','└','├','│']
    special_allow_chars=['.','\n']
    ignore_chars=[char for char in char_catch(text)
                if char not in special_allow_chars
                and char.isalnum()==False 
                and char not in intentSymbol
                ]
    print(
        folder_order(
            text,
            ignore_chars,
            4,
            intentSymbol,
        )
    )
