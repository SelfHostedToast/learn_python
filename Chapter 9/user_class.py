# User Class for imported admin
from privs_class import Privileges
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