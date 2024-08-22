dream_car_list = ['Honda Civic Type R', 'Honda Civic SI', 'Honda Civic Type R']

message = f"There are a lot of cars out there, but I want a {dream_car_list[0]}!"

print(message)

duplicate = 'Honda Civic Type R'

# Using the list.remove method to remove "duplicates" only removes one from the list, this could be critical if say two users had the same username in a web app database, using randomized id's for auth seems way smarter.

dream_car_list.remove(duplicate)

print(dream_car_list)