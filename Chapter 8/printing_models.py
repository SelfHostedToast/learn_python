# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model) 

from printing_functions import print_models as pm
from printing_functions import show_completed_models as cm

# The code below will prime a copy of the unprinted designs list so theat the original may still be referenced.
# print_models(unprinted_designs[:], completed_models)

# 8-15 Printing Models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
cm(completed_models)

print(completed_models)