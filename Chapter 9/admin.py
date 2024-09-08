# 9-7 Admin
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
        

class Admin(User):
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privileges = ['can add posts', 'can delete posts', 'can modify site', 'can moderate users']

    def show_privileges(self):
        print(f'\n{self.first_name} can perform the following actions:')
        for privilege in self.privileges:
                print(f"\t-{privilege}")

dom = Admin('Dominick', 'Smith', 'Carrollton', 23)
dom.show_privileges()
johnny = User('Johnny', 'Ortiz', 'Oak Point', 24)
jacob = User('Jacob', 'Castillo', 'Dallas', 25)
