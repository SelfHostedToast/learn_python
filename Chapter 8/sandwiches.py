# 8-12 Sandwiches

def make_sandwich(*toppings):
    print("Let's begin crafting your sandwich, list your favorite toppings:\n")
    for topping in toppings:
        print(f"\t-adding {topping} to your sandwich")
    print(f"\nYour sandwich is complete with the following toppings on it:")
    for topping in toppings:
        print(f"\t-{topping}")
    print('Thank you for your visit today!\n')

make_sandwich('ham', 'provolone', 'lettuce', 'bacon', 'jalepenos', 'mayo')

make_sandwich('meatballs', 'fresh mozzerella', 'baja chipotle sauce', 'easy lettuce')

make_sandwich('philly steak', 'provolone', 'bell peppers', 'onions', 'baja chipotle sauce')