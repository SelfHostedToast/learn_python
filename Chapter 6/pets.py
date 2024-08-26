# 6-8 Pets

fiona = {
    'pet_name': 'fiona',
    'type': 'cat',
    'owner_name': 'destinie'
}

sonic = {
    'pet_name': 'sonic',
    'type': 'hedgehog',
    'owner_name': 'dominick'
}

cosmo = {
    'pet_name': 'cosmo',
    'type': 'dog',
    'owner_name': 'derek'
}

pets = [fiona, sonic, cosmo]

for pet in pets:
    print(f"{pet['owner_name'].title()} is the proud owner of a {pet['type'].title()} named {pet['pet_name'].title()}!")