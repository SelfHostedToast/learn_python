# 6-9 Favorite Places
favorite_places = {
    'dominick': {
        'place_one': 'dallas',
        'place_two': 'little elm',
        'place_three': 'plano'
    },
    'fawad': {
        'place_one': 'dallas',
        'place_two': 'plano',
        'place_three': 'sachse'
    },
    'david': {
        'place_one': 'home',
        'place_two': 'shandor gardens',
        'place_three': 'weatherford'
    }
}

for person, place in favorite_places.items():
    print(f"{person.title()}'s three favorite places to go are:\n\t-{place['place_one'].title()}\n\t-{place['place_two'].title()}\n\t-{place['place_three'].title()}")