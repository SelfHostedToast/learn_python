# 9-14 Lottery
from random import randint, choice, shuffle

numbers = [0,1,2,3,4,5,6,7,8,9]

letters = ['a','b','c','d','e']

def choose_letters():
    for i in range(0,5):
        random_list.append(letters[randint(0,4)])

def choose_numbers():
    for i in range(0,10):
        random_list.append(numbers[randint(0,9)])

def ticket_letters():
    for i in range(0,5):
        random_lotto.append(letters[randint(0,4)])

def ticket_numbers():
    for i in range(0,10):
        random_lotto.append(numbers[randint(0,9)])

def winning_picks():
    for i in range(0,4):
        winning_lotto.append(choice(random_list))

def my_lotto_list():
    for i in range(0,4):
        my_lotto.append(choice(random_lotto))

my_lotto = []
random_lotto = []
random_list = []
winning_lotto = []
attempts = 0

choose_letters()
choose_numbers()
winning_picks()
ticket_letters()
ticket_numbers()

playing = True

print("Trying your luck...")

while playing == True:
    ticket_letters()
    ticket_numbers()
    my_lotto_list()
    shuffle(my_lotto)
    if my_lotto == winning_lotto:
        print("\n------WINNER------")
        print(f"You win! The ticket matches!\nIt took {attempts} attempts!")
        playing = False
    else:
        my_lotto = []
        random_lotto = []
        attempts += 1

print(f"Your lucky ticket is : {my_lotto}")
print(f"The lottery numbers are: {winning_lotto}")

