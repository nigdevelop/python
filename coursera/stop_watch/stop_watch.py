# template for "Stopwatch: The Game"

import simplegui

# define global variables
time_count = 0
total_stops = 0
sucessful_stops = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenthsec = t%10
    t = t-tenthsec
    min = t/600
    sec = (t%600)/10
    if sec<10:
        sec_str = "0"+str(sec)
    else: 
        sec_str = str(sec)
    return str(min)+":"+sec_str+":"+str(tenthsec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    running = True
    timer.start()

def stop():
    global sucessful_stops, total_stops,time_count, running
    timer.stop()
    if running:
        total_stops = total_stops + 1
        if(time_count%5==0):
            sucessful_stops = sucessful_stops + 1
        running = False
    
def reset():
    global time_count, sucessful_stops, total_stops
    time_count=0
    sucessful_stops = 0  
    total_stops = 0
    
# define event handler for timer with 0.1 sec interval
def time_inc():
    global time_count
    time_count = time_count + 1

# define draw handler
def draw_handler(canvas):
    global time_count
    canvas.draw_text(str(sucessful_stops)+"/"+str(total_stops), (210, 30) , 20, "Green")
    canvas.draw_text(format(time_count), (100, 125) , 30, "White")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 250, 250)

# register event handlers
button1 = frame.add_button('Start', start, 200)
button2 = frame.add_button('Stop', stop, 200)
button3 = frame.add_button('Reset', reset, 200)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
timer = simplegui.create_timer(100, time_inc)

# Please remember to review the grading rubric
