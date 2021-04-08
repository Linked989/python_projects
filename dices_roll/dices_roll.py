import random
from time import sleep

def info():
    print("==================================")
    print("===== Dices Rolling Simulator =====")
    print("==================================")

    print("[r] Roll the dice!")
    print("[q] Quit!")

    select = str(input("Select: "))
    if select == 'r':
        roll()
    elif select == 'q':
        quit()
    else:
        print("Wrong key!")

def roll():
    dice_list = graphics()

    print("Rolling the dices...")
    sleep(1)
    print(random.choice(dice_list))
    print(random.choice(dice_list))

def graphics():
    one = ("""
    -----
    |   |
    | o |
    |   |
    -----
    """)
    two = ("""
    -----
    |o  |
    |   |
    |  o|
    -----
    """)
    three = ("""
    -----
    |o  |
    | o |
    |  o|
    -----
    """)
    four = ("""
    -----
    |o o|
    |   |
    |o o|
    -----
    """)
    five = ("""
    -----
    |o o|
    | o |
    |o o|
    -----
    """)
    six = ("""
    -----
    |o o|
    |o o|
    |o o|
    -----
    """)
    dice_list = [one, two, three, four, five, six]
    return dice_list



if __name__ == '__main__':
    while True:
        info()

