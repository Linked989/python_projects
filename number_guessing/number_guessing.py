import random

numbers = [x for x in range(101)] # Create a list of numbers

print("This is a game where the PC will choose a number and you'll have to guess it!")
print("You will start with a score of '100' points and you'll lose '5' points everytime you guess wrong!")

def menu():
    select = input("Do you want to play? Y/N: ")
    if select == 'y':
        game()
    elif select == 'n':
        quit()

def game():
    score = 105 # Keep count of score
    num = (random.choice(numbers)) # Choose a random number
    print (num)

    while True:
        user = int(input("Your guess: "))
        score -= 5 # Remove score by '5'
        if score == 0:
            print(f"Game over! Your score is '{score}', restart the game!")
            print(f"The correct number was '{num}'!")
            break
        elif user == num:
            print("Good job, you guessed the correct number!")
            print(f"Final score: '{score}'")
            break
        elif user < num:
            print(f"Higher! between")
        elif user > num:
            print(f"Lower!")


menu()



