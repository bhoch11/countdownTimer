#import modules
import time
import sys
from tkinter import *
from tkinter import ttk

HEIGHT = 1024
WIDTH = 1500

root = Tk()
root.title('Countdown Timer')

canvas = Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

time1 = ''
prevSec = ''
minute = 0
seconds = 0
running = False
startTime = 0


top_frame = Frame(root)
top_frame.place(rely = 0.0, relwidth = 1, relheight = 0.9)
timeLeft = ttk.Label(top_frame, text = str(minute) + ':' + str(seconds) , foreground = 'black', background = 'white', anchor = CENTER, font = ('Arial', 400))
timeLeft.pack(fill = BOTH, expand = True)



#begins countdown, loops through minutes and seconds, overwriting original value.
def countdown():
    global minute, seconds, running, prevSec, time1
    if running:
        newSec = time.strftime('%S')
    else:
        newSec = ''
        prevSec = ''
    if newSec != prevSec:
        prevSec = newSec
        seconds -= 1
        if seconds < 0:
            seconds = 59
            minute -= 1
            if minute < 0:
                minute = 0
                seconds = 0
                resetButton.config(state = 'normal')
                startButton.config(state = 'normal')
                stopButton.config(state = 'disabled')
                submitButton.config(state = 'normal')
    if minute > 0:
        timeLeft.config(background = 'white', foreground = 'black')
    else:
        timeLeft.config(background = 'red', foreground = 'white')
    time2 = '{:02d}:{:02d}'.format(minute, seconds)
    if time2 != time1:
        time1 = time2
        timeLeft.config(text= time2)

    timeLeft.after(200, countdown)

countdown()

# setting time based on user input

def setTimer(entryMinute):
    global minute, startTime, time1, seconds, prevSec
    minute = int(entryMinute)
    startTime = int(entryMinute)
    seconds = 0
    prevSec = 0
    running = False
    time1 = '{:02d}:{:02d}'.format(minute, seconds)
    timeLeft.config(text = time1)
    startButton.config(state='normal')
    return minute


def startTime():    # starting clock
    global running, minute
    running = True
    startButton.config(state='disabled')
    stopButton.config(state='normal')
    submitButton.config(state='disabled')
    resetButton.config(state ='disabled')


def stopTime():     #stopping clock
    global running
    running = False
    startButton.config(state = 'normal')
    stopButton.config(state = 'disabled')
    resetButton.config(state = 'normal')
    submitButton.config(state = 'normal')

def resetTime():    #resetting clock
    global minute, seconds, time1, prevSec, running, startTime
    minute = startTime
    seconds = 0
    prevSec = ''
    running = False
    time1 = '{:02d}:{:02d}'.format(minute, seconds)
    timeLeft.config(text = time1)
    startButton.config(state = 'normal')
    stopButton.config(state = 'disabled')
    resetButton.config(state = 'normal')
    submitButton.config(state = 'normal')

# Define the rest of the GUI

bottom_frame = Frame(root)
bottom_frame.place(relx = 0.5, rely = 0.98, anchor = 's' )

ttk.Label(bottom_frame, text = '# of Minutes').grid(row = 0, column = 0, columnspan = 2)

entryMinute = ttk.Entry(bottom_frame, width = 10)
entryMinute.grid(row = 0, column = 2)

submitButton = ttk.Button(bottom_frame, text = 'Set Time', command = lambda: setTimer(entryMinute.get()))
submitButton.grid(row=0, column = 3)

startButton = ttk.Button(bottom_frame, text= 'Start', command = startTime)
startButton.grid(row =1, column = 1)
startButton.config(state = 'disabled')

stopButton = ttk.Button(bottom_frame, text = 'Stop', command = stopTime)
stopButton.grid(row =1, column = 2)
stopButton.config(state = 'disabled')

resetButton = ttk.Button(bottom_frame, text = 'Reset', command = resetTime)
resetButton.grid(row =1, column = 3)
resetButton.config(state = 'disabled')

root.mainloop()


