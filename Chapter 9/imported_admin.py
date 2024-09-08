# 9-11 Imported Admin
from user_class import User
from admin import Admin
from privs_class import Privileges

super_user = Admin('John', 'Doe', 'Unknown', '0')

print(f'Summary of permissions for {super_user.first_name} {super_user.last_name}:')
super_user.privilege.show_privileges()