# 7-6 Three Exits

prompt = "Enter a topping to add to your custom pizza!"
prompt += "\nEnter 'quit' to stop editing your pizza: "

editing_pizza = True

while editing_pizza:
    pizza_toppings = input(prompt)
    if pizza_toppings != 'quit':
        print(f"Adding {pizza_toppings} to your pizza!\n")
    elif pizza_toppings == 'quit':
        print("Exiting...")
        break
    else:
        editing_pizza = False