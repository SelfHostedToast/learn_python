def build_person(first_name, last_name, age=None):
    """return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

me = build_person('dominick', 'smith', age=23)
print(me)