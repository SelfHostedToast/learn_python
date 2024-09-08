# 9-7 Admin
class User:
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.privilege = Privileges()
        
    def describe_user(self):
        print(f"----User information for {self.first_name} {self.last_name}----")
        user_info = [{self.first_name}, {self.last_name}, {self.city}, {self.age}]
        for info in user_info:
            print(info)
    
    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!\n")
        

class Admin(User):
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privilege = Privileges(['can add posts', 'can delete posts', 'can modify site', 'can moderate users'])

class Privileges():

    def __init__(self, privileges=['can add posts', 'can delete own posts']):
        self.privileges = privileges

    def show_privileges(self):

        
        for privilege in self.privileges:
                print(f"\t-{privilege}")

user_1 = Admin('Dominick', 'Smith', 'Carrollton', 23)
print(f'\n{user_1.first_name} can perform the following actions:')
user_1.privilege.show_privileges()

user_2 = User('Johnny', 'Ortiz', 'Oak Point', 24)
print(f'\n{user_2.first_name} can perform the following actions:')
user_2.privilege.show_privileges()

user_3 = User('Jacob', 'Castillo', 'Dallas', 25)
print(f'\n{user_3.first_name} can perform the following actions:')
user_3.privilege.show_privileges()

