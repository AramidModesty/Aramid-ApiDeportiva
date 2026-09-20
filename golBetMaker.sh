mkdir GolBet
cd GolBet
dotnet new sln -n SportsLeague

mkdir GolBet.Entities
cd GolBet.Entities
mkdir Common
cd Common
touch AuditableEntity.cs
cd ../
mkdir Enums
cd Enums
touch MatchStatus.cs
touch BetPick.cs
touch BetStatus.cs
cd ../
touch Team.cs
touch Match.cs
touch Bet.cs
cd ../
mkdir GolBet.Repositories
cd GolBet.Repositories
mkdir Data
cd Data
touch AppDbContext.cs
cd ../
cd ../
