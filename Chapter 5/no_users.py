# username = ['dom','selfhostedtoast', 'domsw0rld', 'admin']
# username = []

if username:
    for user in username:
        if user == 'admin':
            print(f"Hello {user}, would you like to enter configuration mode?")
        else:
            print(f"Hello {user}, welcome to the site!")
else:
    print("We need to find some users!")