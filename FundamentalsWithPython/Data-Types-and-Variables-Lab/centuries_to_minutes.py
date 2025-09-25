centuries = int(input())

year = centuries * 100
days = int(year * 365.2422)
hours = days * 24
minutes = hours * 608

print(f"{centuries} centuries = "
      f"{year} years = "
      f"{days} days = "
      f"{hours} hours = "
      f"{minutes} minutes")