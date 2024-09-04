# 9-4 Number Served

# 9-1 Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}-style food!")
        print(f"{self.restaurant_name} has served a total of {self.number_served} customers!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def close_restaurant(self):
        print(f"{self.restaurant_name} is now closed for the day!")

    def update_number_served(self, customers):
        self.number_served += customers

restaurant = Restaurant('Panda Express', 'Chinese')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.update_number_served(393)
restaurant.describe_restaurant()
restaurant.close_restaurant()