# 9-5 Login Attempts
class User:
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Print User Information in Console"""
        print(f"----User information for {self.first_name} {self.last_name}----")
        user_info = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nCity: {self.city}\nAge: {self.age}\nLogin Attempts: {self.login_attempts}"
        print(user_info)
    
    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        """A Method to increase login attempts in class 'User'"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """A Method to reset login attempts"""
        self.login_attempts = 0

me = User('Dominick', 'Smith', 'Carrollton', 23)
johnny = User('Johnny', 'Ortiz', 'Oak Point', 24)
jacob = User('Jacob', 'Castillo', 'Dallas', 25)

# Describe and Greet myself
User.describe_user(me)
User.greet_user(me)

# Describe and Greet user Johnny
User.describe_user(johnny)
User.greet_user(johnny)

# Describe and Greet user Jacob
User.describe_user(jacob)
User.greet_user(jacob)

# Simulate Login Attempts (15 total)
for i in range(0, 15):
    User.increment_login_attempts(me)
    User.describe_user(me)

# Reset my login attempts
User.reset_login_attempts(me)
User.describe_user(me)