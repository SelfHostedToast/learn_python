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

# Loop through the dictionary and print each key (note that this is the default behavior of looping a dictionary)

for name in favorite_languages.keys():
    print(name.title())

# Set a conditional statement using a list that acts as a filter for the original dictionary, if a user exists within this list, we can do additional operations on the keys specified.

friends = ['phil', 'dominick']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# The keys() method can also be used to check the existence of a particular key utilizing a conditional statement.

if 'selfhostedtoast' not in favorite_languages.keys():
    print("SelfHostedToast, please take our poll!")

# You can sort the keys of a dictionary using the sorted() function, they will sort as they are returned via the for loop we specify

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Most of the same processes can be performed on values using the values() method

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# We notice some duplicate entries, and while in some cases useful, other times we won't need the extra information, to print only unique values we can use a set() to present our data.

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# A set can be built directly using braces and separating the elements with commas:

languages = {'python', 'rust', 'c++', 'c', 'python', 'javascript', 'ruby', 'java', 'python'}
print(sorted(languages))