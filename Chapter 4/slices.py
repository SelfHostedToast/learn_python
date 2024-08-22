# 4-10 Slices

favorite_pizza = ['alfredo', 'bbq chicken', 'pepperoni', 'meat lovers', 'buffalo chicken', 'hawaiian']

for pizza in favorite_pizza:
  print(f"My love for {pizza} pizza should be studied")
print("It's a shame that you can't get a pizza that contains a slice of each kind...")

print(f"The first three items on my favorite pizza list are:\n{favorite_pizza[:3]}")

print(f"Three items from the middle of my favorite pizza list are:\n{favorite_pizza[2:5]} ")

print(f"The last three items on my favorite pizza list are:\n{favorite_pizza[3:]}")