def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello! {username.title()}")

username = input('Enter your username: ')

greet_user(username)