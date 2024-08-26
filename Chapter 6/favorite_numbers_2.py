# 6-10 Favorite Numbers
favorite_numbers = {
    'dominick': {
        'number_one': 21,
        'number_two': 33,
        'number_three': 0
    },
    'fawad': {
        'number_one': 47,
        'number_two': 13,
        'number_three': 7
    },
    'david': {
        'number_one': 1,
        'number_two': 2,
        'number_three': 3
    },
    'derek': {
        'number_one': 7,
        'number_two': 13,
        'number_three': 21
    }
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:\n\t-{numbers['number_one']}\n\t-{numbers['number_two']}\n\t-{numbers['number_three']}")