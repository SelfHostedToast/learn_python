players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Print a slice of the list, index from start to end omitting the last result specified
print(players[0:3])

# The same idea for any subset of the list

print(players[1:4])

# You can specify a slice to start from anywhere in the list index and go to the end

print(players[3:])

# If the beggining index isn't specified, the slice starts there

print(players[:3])

# You can slice from the end of a list as well

print(players[-2:])

print(players[:-2])