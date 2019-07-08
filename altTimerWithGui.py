
#import modules
import time
import sys
from tkinter import *
from tkinter import ttk

HEIGHT = 700
WIDTH = 800

# Function for obtaining a minute value and validating it.
def chooseMinute():
        global minute
        try:
            minute = int(input())
        except ValueError:
            print('That is not a valid integer, try again')
            chooseMinute()
        if minute > -1:
            return minute
        else:
            print('Please enter a non-negative integer')
            chooseMinute()

# Function for obtaining a seconds value and validating it.
def chooseSeconds():
        global seconds
        try:
            seconds = int(input())
        except ValueError:
            print('That is not a valid integer, try again')
            chooseSeconds()
        if seconds > -1 and seconds < 60:
            return seconds
        else:
            print('Please enter a value between 0 and 59')
            chooseSeconds()



#begins countdown, loops through minutes and seconds, overwriting original value.
def countdown(minute, seconds):
        if minute == 0 and seconds == 0:
                sys.stdout.write("\r" + '{:02d}:{:02d}'.format(minute, seconds))
                return 0
        else:
                sys.stdout.write("\r" + '{:02d}:{:02d}'.format(minute, seconds))
                sys.stdout.flush()
                time.sleep(1)
                seconds = 60
                countdown(minute - 1, seconds -1)
        #else:
               #sys.stdout.write("\r" + '{:02d}:{:02d}'.format(minute, seconds))
        sys.stdout.flush()
        time.sleep(1)
        countdown(minute, seconds - 1)

def test_function(entry):
    print('This is the entry: ',entry)
    label['text'] = entry

'''
#running the program.
print('Please enter a value for Minutes')
chooseMinute()

print('Please enter a value for Seconds')
chooseSeconds()

print('beginning countdown')
countdown(minute, seconds)
'''

root = Tk()

canvas = Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

top_frame = Frame(root, background = 'blue')
top_frame.place(relx = 0.1, rely = 0.05, relwidth = 0.8, relheight = 0.8)
label = ttk.Label(top_frame, text = '0:00', background = 'white', anchor = CENTER, font = ('Arial', 120))
label.pack(fill = BOTH, expand = True)

bottom_frame = Frame(root, background = 'green')
bottom_frame.place(relx = 0.5, rely = 0.98, relwidth = 0.8, relheight = 0.1, anchor = 's' )


entry = ttk.Entry(bottom_frame)
entry.pack(fill = X, expand = True)

startButton = ttk.Button(bottom_frame, text= 'Start', command= lambda: test_function(entry.get()))
startButton.pack(side = LEFT, fill = X, expand = TRUE)

stopButton = ttk.Button(bottom_frame, text = 'Stop')
stopButton.pack(side = LEFT, fill = X, expand = TRUE)

resetButton = ttk.Button(bottom_frame, text = 'Reset')
resetButton.pack(side = LEFT, fill = X, expand = TRUE)



root.mainloop()
