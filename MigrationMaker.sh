#Migracion de base de datos
cd SportsLeague
#Crea la migracion
dotnet ef migrations add InitialCreate --project SportsLeague.DataAccess --startup-project SportsLeague.API

#Aplica la migración a la base de datos
dotnet ef database update --project SportsLeague.DataAccess --startup-project SportsLeague.API
