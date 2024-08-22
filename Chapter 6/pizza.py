# Store information about a pizza being ordered.

pizza = {
    'crust': 'pan',
    'toppings': ['pepperoni', 'extra cheese', 'philly steak'],
    'sauce': 'alfredo'
}

# Summarize the order

print(f"You ordered a {pizza['crust']} style pizza, with {pizza['sauce']} sauce.\nHere is the list of ingredients on your pizza:")

for topping in pizza['toppings']:
    print(f"\t-{topping}")