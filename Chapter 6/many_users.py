users = {
    'dsmith': {
        'first': 'dominick',
        'last': 'smith',
        'location': 'texas',
    },
    'jdoe': {
        'first': 'john',
        'last': 'doe',
        'location': 'unknown',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")