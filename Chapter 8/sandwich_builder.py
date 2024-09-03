def make_sandwich(*toppings):
    print("Let's begin crafting your sandwich, list your favorite toppings:\n")
    for topping in toppings:
        print(f"\t-adding {topping} to your sandwich")
    print(f"\nYour sandwich is complete with the following toppings on it:")
    for topping in toppings:
        print(f"\t-{topping}")
    print('Thank you for your visit today!\n')