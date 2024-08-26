# 7-3 Multiples of Ten

prompt = "This program will determine if a number is a multiple of ten.\n"
prompt += "Enter a number here: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")