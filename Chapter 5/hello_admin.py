user_database = ['admin', 'dom', 'selfhostedtoast', 'domsw0rld', 'opzylo']

username = ''

user_input = str(input('Enter a username\n'))

username = user_input

user_exist = False

for user in user_database:
    if username == user and username == 'admin':
        print(f"Hello {user}, would you like to enter configuration mode?")
        user_exist = True
        break
    elif username == user:
        print(f"Hi {user}, welcome to the site!")
        user_exist = True
        break
else:
    if user_exist == False:
        print("No user with that name exists...")