# A list is a collection of items in a particular order.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Print a specific entry of a list using its index as reference

print(bicycles[0])

# From here you can format the consoles output to any formatting

print(bicycles[0].title())

# You can return the last element of any list by returning the index of -1

print(bicycles[-1].upper())

# The same premise exists for the second to last, third to last, etc by doing -n

print(bicycles[-3].lower())

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)