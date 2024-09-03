# 8-13 User Profile

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
# The function build_profile can take any number of key - value pairs to add to the dictionary, notated by ** (this is often expressed as **kwargs in a function)

user_profile = build_profile('Dominick','Smith', favorite_color='blue', location='Texas', favorite_food='hot dogs')

print(user_profile)