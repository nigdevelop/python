# implementation of card game - Memory

import simplegui
import random

numbers =[]
display=[]
RECTANGLE_WIDTH=50
state = 0
turns = 0
click1 = -1
click2 = -1

# helper function to initialize globals
def new_game():
    global numbers, display, turns, label
    turns = 0
    array1 = range(0,8)  
    array2 = range(0,8)  
    numbers = array1 + array2
    random.shuffle(numbers)
    display = [False for x in range(16)]
    label.set_text("Turns = "+str(turns))  
    
def rectangle_clicked(xpos):
    clicked = xpos/RECTANGLE_WIDTH
    return clicked

# define event handlers
def mouseclick(pos):
    global click1, click2, numbers, display, state, label, turns
    card = rectangle_clicked(pos[0])
    # add game state logic here
    if(not display[card]):
        display[card] = True
        if state == 0:
            click1 = card
            state = 1
        elif state == 1:
            click2 = card
            state = 2
        else:
            if(numbers[click1] != numbers[click2]):
                display[click1] = False
                display[click2] = False 
            click1 = card    
            state = 1
            turns += 1
    label.set_text("Turns = "+str(turns))  
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers, display
    i = 0
    for num in numbers:
        if display[i]:
            canvas.draw_text(str(num), (i*RECTANGLE_WIDTH + 20,60), 30, "White")
        else:    
            canvas.draw_polygon([(i*RECTANGLE_WIDTH, 0), ((i+1)*RECTANGLE_WIDTH, 0), 
                             ((i+1)*RECTANGLE_WIDTH, 100) ,(i*RECTANGLE_WIDTH, 100)], 3, "White", "Green")
        i=i+1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric