current_users = ['user1', 'user2', 'user3', 'dominick', 'admin']

new_users = ['DOMINICK', 'user4', 'user5', 'monty', 'ADMIN']

new_users_validate = []

print("Checking username...\n")

for user in new_users:
    user = user.lower()
    new_users_validate.append(user)

for username in new_users_validate:
    if username in current_users:
        print(f"The username {username} is already in use.\nPlease select another username.\n")
    elif username:
        print(f"{username} is available!\n")
    else:
        print("An error has occured")
        break