ask_user_age = int(input("Enter your age\n"))

user_age = ask_user_age

if user_age < 2:
    print("You are literally a baby.")
elif user_age >= 2 and user_age < 4:
    print("You are a toddler.")
elif user_age >= 4 and user_age < 13:
    print("You are a kid.")
elif user_age >= 13 and user_age < 20:
    print("You are a teenager")
elif user_age >= 20 and user_age < 65:
    print("You are an adult")
elif user_age > 65:
    print("You are an elder")
else:
    print("That is not a valid age")