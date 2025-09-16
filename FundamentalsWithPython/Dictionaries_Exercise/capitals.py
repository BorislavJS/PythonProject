countries = input().split(", ")
capitals = input().split(", ")

country_capital = {}

# country_capital = {country: capital for country, capital in zip(countries, capitals)}
for country, capital in zip(countries, capitals):
    country_capital[country] = capital

for key, value in country_capital.items():
    print(f"{key} -> {value}")