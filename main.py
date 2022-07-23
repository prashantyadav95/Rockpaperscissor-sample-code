# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

def game():
    player=input("r for 'rock', s for 'scissor', p for 'paper' Whats your choice? ")
    computer = random.choice(['r', 'p', 's'])
    print("Computers choice - ",computer)

    if player == computer:
        print("Its a Tie!!")

    if winner(player,computer):
        print("You Won!!!")
    else:
        print("You Loose!!")

def winner(user,opponent):
    if(user == 'r' and opponent == 's') or (user == 'p' and opponent == 'r') or (user == 's' and opponent == 'p'):
        return True
game()

