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
        user_info = {'First Name' : {self.first_name},
        'Last Name' : {self.last_name},
        'City' : {self.city},
        'Age' : {self.age}}
        for info_type, info in user_info.items():
            print(f'{info_type} : {info}')
    
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
user_2 = User('Johnny', 'Ortiz', 'Oak Point', 24)
user_3 = User('Jacob', 'Castillo', 'Dallas', 25)

# web_users = [user_1, user_2, user_3]

# for web_user in web_users:
#     web_user.greet_user()
#     web_user.describe_user()
#     print(f'\n{web_user.first_name} can perform the following actions:')
#     web_user.privilege.show_privileges()