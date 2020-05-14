# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

hi_bound = 100


# helper function to start and restart the game
def new_game(hbound):
    # begins a new game, initializes the computers guess,
    # and picks a number in a defined range
    global secret_number
    global hi_bound
    global it_guess
    hi_bound = hbound
    if hi_bound == 100:
        guesses = 7
    else:
        guesses = 10
    it_guess = guesses
    secret_number = random.randrange(0, hi_bound)
    print "New game started, you have " + str(guesses) + " guesses"
    print " "
    # print secret_number


# define event handlers for control panel
def range100():
    # Set high bounding to range as 100 and start a new game
    new_game(100)

def range1000():
    # Set high bounding to range as 1000 and start a new game
    new_game(1000)
    
def input_guess(guess):
    # Takes input from the user as a guess	
    hg = int(guess)
    global it_guess
    global hi_bound
    it_guess = it_guess - 1
    print "Guess was", hg
    global secret_number
    if hg - secret_number > 0:
        print "Lower"
        if it_guess < 1:
            print "Game over, dude!"
            print " "
            new_game(hi_bound)
        else:
            print "You have " + str(it_guess) + " guesses remaining"
        print " "
    elif hg - secret_number < 0:
        print "Higher"
        if it_guess < 1:
            print "Game over, dude!"
            print " "
            new_game(hi_bound)
        else:
            print "You have " + str(it_guess) + " guesses remaining"
        print " "
    else: 
        print "Correct!"
        print " "
        new_game(hi_bound)
    

    
# create frame
frame = simplegui.create_frame("Guess a number",400,400)
frame.add_input("Enter your guess:", input_guess, 100)
frame.add_button("New Game, Range is [0,100) ", range100, 200)
frame.add_button("New Game, Range is [0,1000) ", range1000, 200)

# register event handlers for control elements and start frame


# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
