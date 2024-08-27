# 7-9 No Pastrami

sandwich_orders = ['blt', 'ham and cheddar', 'turkey bacon ranch', 'ham and provolone', 'pastrami', 'pastrami', 'pastrami', 'turkey club', 'grilled cheese', 'chopped brisket']

finished_sandwiches = []

print("We are all out of Pastrami for the day!")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        del(current_sandwich)
    else:
        print(f"Preparing your {current_sandwich}!")
        finished_sandwiches.append(current_sandwich)

for sandwich in sorted(finished_sandwiches):
    print(sandwich)