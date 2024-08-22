favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'dominick': 'python',
}

poll_users = ['dominick', 'phil', 'edward', 'sarah', 'jen', 'thomas', 'johnny', 'mario', 'alex', 'jacob']

for name in sorted(poll_users):
    if name in sorted(favorite_languages.keys()):
        print(f"Hello {name.title()}!\nThank you for taking the poll\nI see your favorite language is {favorite_languages[name].title()}!\n")
    elif name not in favorite_languages.keys():
        print(f"Hello {name.title()},\nPlease complete the favorite languages poll.\n")