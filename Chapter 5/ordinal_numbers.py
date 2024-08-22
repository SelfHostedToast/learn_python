number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("The following are the grade levels of K-12 Schooling:\n")

for number in number_list:
    if number == 1:
        number_list[number -1] = '1st'
        print(f"{number_list[number -1]}\n")
    elif number == 2:
        number_list[number -1] = '2nd'
        print(f"{number_list[number -1]}\n")
    elif number == 3:
        number_list[number -1] = '3rd'
        print(f"{number_list[number -1]}\n")
    else:
        number_list[number -1] = f'{number}th'
        print(f"{number_list[number -1]}\n")