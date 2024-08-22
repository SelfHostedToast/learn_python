# A tuple is a static list, can't be changed once defined.

dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# The difference with tuples vs with lists, is that tuples can be re-assigned via the = operator.

print(f"Original dimensions:")
for dimension in dimensions:
  print(dimension)

# Re-assign the tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
  print(dimension)