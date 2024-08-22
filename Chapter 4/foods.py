my_foods = ['pizza', 'fried rice', 'brownies']

friend_foods = my_foods[:]

print(f"My favorite foods are:\n{my_foods}")

print(f"My friend's favorite foods are:\n{friend_foods}")

# This example shows two different lists, containing the same values. Think of not specifying any indices in a list range as copying it as a starting point from start to finish

my_foods.append('bollios')
friend_foods.append('cheeseburgers')

print(f"My favorite foods are:\n{my_foods}")

print(f"My friend's favorite foods are:\n{friend_foods}")

# Notice the two lists are different even though we set them equal at first

for food in my_foods:
  print(food)

for food in friend_foods:
  print(food)