favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'dominick': 'python',
}

language = favorite_languages['dominick'].title()
print(f"Dominick's favorite language is {language}.")

# Looping through the dictionary, because the keys and values are the same type, we can generalize them into unique variable names for key and value respectively.

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")