# 3-8 Seeing The World

travel_locations = ['switzerland', 'spain', 'canada', 'hawaii', 'france', 'london', 'mexico', 'tokyo', 'dubai']

# Printing the list in its original order.

print(travel_locations)

# Printing the sorted list temporarily sorted alphabetically (order does not change)

print(sorted(travel_locations))

# Printing the list to confirm it has not changed

print(travel_locations)

print(sorted(travel_locations, reverse=True))

# Demonstrate the list hasn't changed

print(travel_locations)

# Reverse the list permanently
travel_locations.reverse()

print(travel_locations)

# Undo the reverse function
travel_locations.reverse()

print(travel_locations)

# Sort list alphabetically
travel_locations.sort()

print(travel_locations)

# Sort list reverse-alphabetically
travel_locations.sort(reverse=True)

print(travel_locations)