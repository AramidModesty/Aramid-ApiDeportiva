# Desarrollado en linux

# Crea carpeta
mkdir SportsLeague
cd SportsLeague

# Crea solucion
dotnet new sln -n SportsLeague

# Crea Proyecto API (Web API)
dotnet new webapi -n SportsLeague.API -controllers
 
# Crea Proyecto Domain (Class Library)
dotnet new classlib -n SportsLeague.Domain
 
# Crea Proyecto DataAccess (Class Library)
dotnet new classlib -n SportsLeague.DataAccess

# Add proyecto web API a la solucion
dotnet sln add SportsLeague.API/SportsLeague.API.csproj

# Add proyecto Domain a la solucion
dotnet sln add SportsLeague.Domain/SportsLeague.Domain.csproj

# Add proyecto DataAccess a la solucion
dotnet sln add SportsLeague.DataAccess/SportsLeague.DataAccess.csproj

# API referencia a Domain
dotnet add SportsLeague.API/SportsLeague.API.csproj reference SportsLeague.Domain/SportsLeague.Domain.csproj
 
# API referencia a DataAccess (para registrar servicios en Program.cs)
dotnet add SportsLeague.API/SportsLeague.API.csproj reference SportsLeague.DataAccess/SportsLeague.DataAccess.csproj
 
# DataAccess referencia a Domain
dotnet add SportsLeague.DataAccess/SportsLeague.DataAccess.csproj reference SportsLeague.Domain/SportsLeague.Domain.csproj

# Elimina los archivos automaticamente creados en domain y DataAccess
# Linux / Mac
rm SportsLeague.Domain/Class1.cs
rm SportsLeague.DataAccess/Class1.cs

#Crear carpetas en estructuras:

cd SportsLeague.Domain
mkdir Entities
mkdir Enums
mkdir Interfaces
cd Interfaces
mkdir Repositories
mkdir Services
cd ../
mkdir Services
cd ../ #Fin SportsLeague

cd SportsLeague.DataAccess
mkdir Context
mkdir Repositories
mkdir Migrations
cd .. #Fin DataAccesss

mkdir SportsLeague.API
cd SportsLeague.API
mkdir Controllers
mkdir DTOs
cd DTOs
mkdir Request
mkdir Response
cd ../
mkdir Mappings
mkdir Middlewares
cd ../ #Fin API

#Instalar Paquetes NuGet

cd SportsLeague.DataAccess
dotnet add package Microsoft.EntityFrameworkCore -v 8.0.*
dotnet add package Microsoft.EntityFrameworkCore.SqlServer -v 8.0.*
dotnet add package Microsoft.EntityFrameworkCore.Tools -v 8.0.*
cd ..

cd SportsLeague.API
dotnet add package Microsoft.EntityFrameworkCore.Design -v 8.0.*
dotnet add package AutoMapper.Extensions.Microsoft.DependencyInjection
dotnet add package Swashbuckle.AspNetCore
cd ..

cd SportsLeague.Domain
dotnet add package Microsoft.Extensions.Logging.Abstractions
cd ..
