# 9-2 Three Restaurants

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}-style food!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant_one = Restaurant('Panda Express', 'Chinese')
restaurant_two = Restaurant('Babes Chicken', 'American')
restaurant_three = Restaurant('Taco Bell', 'Tex-Mex')

restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()