# 9-3 Users

class User:
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    def describe_user(self):
        print(f"----User information for {self.first_name} {self.last_name}----")
        user_info = [{self.first_name}, {self.last_name}, {self.city}, {self.age}]
        for info in user_info:
            print(info)
    
    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!\n")

me = User('Dominick', 'Smith', 'Carrollton', 23)
johnny = User('Johnny', 'Ortiz', 'Oak Point', 24)
jacob = User('Jacob', 'Castillo', 'Dallas', 25)

User.describe_user(me)
User.greet_user(me)

User.describe_user(johnny)
User.greet_user(johnny)

User.describe_user(jacob)
User.greet_user(jacob)