#import modules
import time
import sys

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
        elif seconds ==0:
                sys.stdout.write("\r" + '{:02d}:{:02d}'.format(minute, seconds))
                sys.stdout.flush()
                time.sleep(1)
                seconds = 60
                countdown(minute - 1, seconds -1)
        else:
                sys.stdout.write("\r" + '{:02d}:{:02d}'.format(minute, seconds))
        sys.stdout.flush()
        time.sleep(1)
        countdown(minute, seconds - 1)


#running the program.
print('Please enter a value for Minutes')
chooseMinute()

print('Please enter a value for Seconds')
chooseSeconds()

print('beginning countdown')
countdown(minute, seconds)
