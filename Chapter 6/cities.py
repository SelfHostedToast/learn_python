# 6-11 Cities

cities = {
    'dallas': {
        'country': 'USA',
        'population': 1_302_753,
        'fact': "The world's first convenience store, 7-Eleven, opened in 1927 in Dallas. The corporation is still headquartered here today."
    },
    'zurich': {
        'country': 'Switzerland',
        'population': 1_443_000,
        'fact': "The University of Zürich is one of Europe’s oldest universities."
    },
    'tokyo': {
        'country':'Japan',
        'population': 37_115_035,
        'fact': "There is one vending machine per every 23 people living in the city."
    }
}

for city, city_information in cities.items():
    print(f"{city.title()} is a city located in {city_information['country']}.\nIt has a population of {city_information['population']}!\nLastly, a cool fact about {city.title()} is that {city_information['fact']}.\n")