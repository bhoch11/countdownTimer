import time
import sys
import tkinter

#begins countdown, loops through minutes and seconds, prints each value
def countdown():
        global minute
        global seconds
        print('beginning countdown')
        if minute > 0 and seconds == 0:  ## working
                sys.stdout.write(str(minute)+':0'+str(seconds))
                sys.stdout.flush()
                time.sleep(1)
                minute = minute - 1
                seconds = 59
                for num in range(0, minute + 1):
                        for num in range(0, 60):
                                if seconds >= 10:
                                        sys.stdout.write(str(minute) +':'+str(seconds))
                                        sys.stdout.flush()
                                else:
                                        sys.stdout.write(str(minute)+':0'+str(seconds))
                                        sys.stdout.flush()
                                seconds = seconds - 1
                                time.sleep(1)
                        minute = minute - 1
                        seconds = 59
                        
        elif minute > 0 and seconds > 0:  ## working
                for num in range(0, minute + 1):
                        for num in range(0 , seconds + 1):
                                if seconds >= 10:
                                        sys.stdout.write(str(minute)+':'+str(seconds))
                                        sys.stdout.flush()
                                else:
                                        sys.stdout.write(str(minute)+':0'+str(seconds))
                                        sys.stdout.flush()
                                seconds -= 1
                                time.sleep(1)
                        minute = minute - 1
                        seconds = 59
                        
        else:                           ## working
                for num in range(0, seconds + 1):
                        if seconds >= 10:
                                sys.stdout.write(str(minute)+':'+str(seconds))
                                sys.stdout.flush()
                        else:
                                sys.stdout.write(str(minute)+':0'+str(seconds))
                                sys.stdout.flush()
                        seconds = seconds - 1
                        time.sleep(1)

                             
#takes user input to store in variable                
print('Please enter a minute value')
minute = int(input())
print('Please enter a second value')
seconds = int(input())

#program function calls		
countdown()


