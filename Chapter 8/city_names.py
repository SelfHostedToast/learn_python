# 8-6 City Names

def city_country(city_name, country):
    return(f'"{city_name.title()}, {country.title()}"')

print(city_country('dallas','usa'))
print(city_country('tokyo','japan'))
print(city_country('zurich','switzerland'))