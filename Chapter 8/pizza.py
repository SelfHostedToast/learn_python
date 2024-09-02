def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t-{topping}")

make_pizza('pepperoni', 'philly steak', 'pineapple')

make_pizza('cheese')