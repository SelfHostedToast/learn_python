cars = ['toyota', 'chevorlet', 'kia', 'honda']
# Assuming your list is all lowercase, we can use the sort method to sort a list alphabetically
cars.sort()

print(cars)

# Reverse sort method
cars.sort(reverse=True)
print(cars)

# We can also temporarily sort a list to maintain its original order. We use the sorted() function

print(f"The original list:{cars}")

print(f"\nHere is the sorted list:{sorted(cars)}")

print(f"\nHere is the original list once again:{cars}")

# Print the list in reverse order

cars.reverse()
print(cars)

# Printing the length of a list (element-wise)

print(len(cars))

