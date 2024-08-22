major_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'ganges': 'india',
    'thames': 'england'
}

for river, country in major_rivers.items():
    print(f"The {river.title()} river flows through the country of {country.title()}!")

# Embarrasing fact of this project is that I needed to look up if India & if England were countries...