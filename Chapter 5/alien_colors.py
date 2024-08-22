ask_alien_color = str(input("Enter a color\n"))

alien_color = ask_alien_color.lower()

if alien_color == 'green':
    print('You have earned 5 points!')
elif alien_color == 'yellow':
    print('You have earned 10 points!')
elif alien_color == 'red':
    print("You have earned 15 points")
else:
    print("You did not earn any points...")