# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

secret_num = 0
num_of_guesses = 0
upper_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_num, upper_range, num_of_guesses
    print ""
    print "New game. Range is from 0 to " + str(upper_range)
    #2 ** n >= high - low + 1
    num_of_guesses = int(math.log(upper_range - 0, 2) + 1)
    print "Number of guesses is " + str(num_of_guesses)
    secret_num = random.randrange(0, upper_range)
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global upper_range
    upper_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    global upper_range
    upper_range = 1000
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global secret_num, num_of_guesses
    num_guessed = int(guess)
    print ""
    print "Guess was "+guess
    num_of_guesses = num_of_guesses-1
    print "Num of remaning guesses is "+str(num_of_guesses)
    if(num_guessed > secret_num):
        print "Lower!"
    elif(num_guessed < secret_num):
        print "Higer!"
    else:
        print "Correct!"
        new_game()
        
    if(num_of_guesses == 0):
        print "You Lose!!!"
        print ""
        new_game()
    
  
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button('Range is [0 to 100)', range100, 150)
frame.add_button('Range is [0 to 1000)', range1000, 150)
frame.add_input('Enter a Guess', input_guess, 100)
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
