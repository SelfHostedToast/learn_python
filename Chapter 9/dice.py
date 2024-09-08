# 9-13 Dice

from random import randint as ri

def roll_die(sides):
    x = 1
    for i in range(1, sides + 1):
        print(f"Generated: {ri(1,sides)} ({x})")
        x += 1
    print("--------------------")

roll_die(6)
roll_die(10)
roll_die(20)