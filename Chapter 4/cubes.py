# 4-8 Cubes

cubes = []
for value in range(1,11):
  value = value ** 3
  cubes.append(value)
print(cubes)

# 4-9 Cube Comprehension

cube_comprehension = [value ** 3 for value in range(1,11)]
print(cube_comprehension)