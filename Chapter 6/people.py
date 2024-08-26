dsmith = {'first_name': 'Dominick', 'last_name': 'Smith', 'age': 23, 'city': 'Carrollton', 'username': 'dsmith'}

jdoe = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 1337,
    'city': 'worldwide',
    'username': 'jdoe'
}

jwick = {
    'first_name': 'john',
    'last_name': 'wick',
    'age': 54,
    'city': 'new jersey',
    'username': 'jwick'
}

people = [dsmith, jdoe, jwick]

for person in people:
    print(f"Report for {person['username']}:")
    print(f"\t- First Name: {person['first_name'].title()}")
    print(f"\t- Last Name: {person['last_name'].title()}")
    print(f"\t- Age: {person['age']}")
    print(f"\t- City: {person['city'].title()}\n")