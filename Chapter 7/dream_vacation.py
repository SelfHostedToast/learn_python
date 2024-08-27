# 7-10 Dream Vacation

responses = {}

polling_active = True

while polling_active:
    name = input("\nEnter your name: ")
    last_name = input("\nEnter your last name: ")
    response = input("\nWhere would you take your dream vacation? ")

    responses[name, last_name] = response
    # responses[last_name] = response

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name[0].title()} {name[1].title()} would like to go {response.title()}.")