
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
        print('beginning countdown')
        if minute > 0 and seconds == 0:  ## working
                sys.stdout.write("\r" + str(minute)+':0'+str(seconds))
                sys.stdout.flush()
                time.sleep(1)
                minute = minute - 1
                seconds = 59
                for num in range(0, minute + 1):
                        for num in range(0, 60):
                                if seconds >= 10:
                                        sys.stdout.write("\r" + str(minute) +':'+str(seconds))
                                        sys.stdout.flush()
                                else:
                                        sys.stdout.write("\r" + str(minute)+':0'+str(seconds))
                                        sys.stdout.flush()
                                seconds = seconds - 1
                                time.sleep(1)
                        minute = minute - 1
                        seconds = 59

        elif minute > 0 and seconds > 0:
                for num in range(0, minute + 1):
                        for num in range(0 , seconds + 1):
                                if seconds >= 10:
                                        sys.stdout.write("\r" + str(minute)+':'+str(seconds))
                                        sys.stdout.flush()
                                else:
                                        sys.stdout.write("\r" + str(minute)+':0'+str(seconds))
                                        sys.stdout.flush()
                                seconds -= 1
                                time.sleep(1)
                        minute = minute - 1
                        seconds = 59

        else:                           ## working
                for num in range(0, seconds + 1):
                        if seconds >= 10:
                                sys.stdout.write("\r" + str(minute)+':'+str(seconds))
                                sys.stdout.flush()
                        else:
                                sys.stdout.write("\r" + str(minute)+':0'+str(seconds))
                                sys.stdout.flush()
                        seconds = seconds - 1
                        time.sleep(1)


#running the program.
print('Please enter a value for Minutes')
chooseMinute()

print('Please enter a value for Seconds')
chooseSeconds()

countdown(minute, seconds)
