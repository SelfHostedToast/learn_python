# 7-8 Deli

sandwich_orders = ['blt', 'ham and cheddar', 'turkey bacon ranch', 'ham and provolone']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am preparing the {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)