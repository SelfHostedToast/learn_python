# 7-5 Movie Tickets

prompt = "Enter your age to see the price of your ticket."
prompt += "\nEnter '0' to exit the program:\n"

running = True


while running:
    age = input(prompt)
    age = int(age)

    if age == 0:
        running = False
    elif age < 3:
        ticket_cost = 0
        print(f"\nThe cost of your ticket is \n\t${ticket_cost}.\n")
    elif age >= 3 and age <= 12:
        ticket_cost = 10
        print(f"\nThe cost of your ticket is \n\t${ticket_cost}.\n")
    elif age > 12:
        ticket_cost = 15
        print(f"\nThe cost of your ticket is \n\t${ticket_cost}.\n")
    else:
        print("Please enter a valid age...\n")
