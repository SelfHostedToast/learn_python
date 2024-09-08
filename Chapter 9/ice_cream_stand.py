# 9-6 Ice Cream Stand
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!\n")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'cappacino', 'birthday cake', 'rocky road']

    def list_flavors(self):
        print("We have the following flavors of ice cream available:")
        for flavor in self.flavors:
            print(f"\t-{flavor}")

restaurant = Restaurant('Panda Express', 'Chinese')

restaurant.describe_restaurant()
restaurant.open_restaurant()

parlor = IceCreamStand("Andy's Frozen Custard", 'Ice Cream')

parlor.describe_restaurant()
parlor.open_restaurant()
parlor.list_flavors()