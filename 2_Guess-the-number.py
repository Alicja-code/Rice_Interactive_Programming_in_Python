# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_number
    global chances
    secret_number = random.randrange(0, num_range)
    print
    "New game. Range is [0,", num_range, ")"
    chances = int(math.ceil((math.log(num_range, 2))))
    print
    "Number of remaining guesses is", chances
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    guess = int(guess)
    print
    "Guess was", guess
    global chances
    chances = chances - 1
    print
    "Number of remaining guesses is", chances
    if chances > 0:
        if guess == secret_number:
            print
            "Correct! \n"
            new_game()
        elif guess > secret_number:
            print
            "Lower! \n"
        elif guess < secret_number:
            print
            "Higher! \n"
        else:
            print
            "Sth is wrong \n"
    elif chances == 0:
        if guess == secret_number:
            print
            "Correct! \n"
            new_game()
        elif guess != secret_number:
            print
            "You ran out of guesses. The number was", secret_number
            print
            new_game()
        else:
            print
            "Sth is wrong \n"
    else:
        print
        "Sth is wrong \n"


# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
frame.add_input("Enter guess", input_guess, 100)
frame.start()

# call new_game
new_game()
