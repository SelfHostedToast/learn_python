def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

animal_type_prompt = input("Enter what kind of pet you have: ")

pet_name_prompt = input("Enter your pets name: ")

describe_pet(pet_name_prompt, animal_type_prompt)
describe_pet('fiona', 'cat')
describe_pet(animal_type='dog', pet_name='sparky')
describe_pet(pet_name='sparky', animal_type='dog')
describe_pet('fiona')

