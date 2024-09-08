# 9-7 Admin
from user_class import User
from privs_class import Privileges
class Admin(User):
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privilege = Privileges(['can add posts', 'can delete posts', 'can modify site', 'can moderate users'])

# user_1 = Admin('Dominick', 'Smith', 'Carrollton', 23)
# user_2 = User('Johnny', 'Ortiz', 'Oak Point', 24)
# user_3 = User('Jacob', 'Castillo', 'Dallas', 25)

# web_users = [user_1, user_2, user_3]

# for web_user in web_users:
#     web_user.greet_user()
#     web_user.describe_user()
#     print(f'\n{web_user.first_name} can perform the following actions:')
#     web_user.privilege.show_privileges()