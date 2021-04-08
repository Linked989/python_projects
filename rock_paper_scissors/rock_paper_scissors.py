import random
from time import sleep
import os

comp_choice = ['rock', 'paper', 'scissors']

def user_choice():
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    print("[q] Quit!")

    user = (input("Make your choice: ") )
    print()

    if user == 'q':
        print("Bye!")
        quit()

    return user

def game():
    rock,paper,scissors,draw = ascii()

    user = int(user_choice())
    # sleep(3)
    print("AI is thinking!...")
    ai = random.choice(range(0,3))

    print(f"User chose: {comp_choice[user - 1]} <===")
    print(f"AI chose: {comp_choice[ai]} <===")

    # Rules!!!
    # Draw
    if (user == 1 and ai == 0) or (user == 2 and ai == 1) or (user == 3 and ai == 2):
        print("Draw!")
        print(draw)
    # User wins!
    if (user == 1 and ai == 2): # r vs s
        print("You win!")
        print(f"User: {rock} and Computer: {scissors}")
    if (user == 2 and ai == 0): # p vs r
        print("You win!")
        print(f"User: {paper} and Computer: {rock}")
    if (user == 3 and ai == 1): # s vs p
        print("You win!")
        print(f"User: {scissors} and Computer: {paper}")

    # Computer wins!
    if (user == 1 and ai == 1): # r vs p
        print("AI wins!")
        print(f"User: {rock} and Computer: {paper}")
    if (user == 2 and ai == 2): # p vs s
        print("AI wins!")
        print(f"User: {paper} and Computer: {scissors}")
    if (user == 3 and ai == 0): # s vs r
        print("AI wins!")
        print(f"User: {scissors} and Computer: {rock}")
    

def ascii():
    # Rock  
    rock = ("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    # Paper
    paper = ("""
        _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    # Scissors
    scissors = ("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    draw = ("""
     ____                      _ 
    |  _ \ _ __ __ ___      _| |
    | | | | '__/ _` \ \ /\ / / |
    | |_| | | | (_| |\ V  V /|_|
    |____/|_|  \__,_| \_/\_/ (_)
 """)
    return rock,paper,scissors,draw


while True:
    if __name__ == "__main__":
        game()


