from tkinter import *
from tkinter import ttk



class countdownTimer:

    def __init__(self, master):

        master.title('Countdown Timer')
        master.configure(background = 'white')

        self.style = ttk.Style()
        self.style.configure('timer.TFrame', background = 'white')
        self.style.configure('input.TFrame', background = 'black')

        self.timerFrame = ttk.Frame(master)
        self.timerFrame.pack()
        self.timer = ttk.Label(self.timerFrame, text = '3:00', background = 'white', font = ('Arial', 600)).pack(fill = BOTH, expand = True)



        self.inputFrame = ttk.Frame(master)
        self.inputFrame.pack(side = BOTTOM)
        self.start = ttk.Button(self.inputFrame, text = 'start', command = self.startButton).grid(row =0, column = 0)
        self.stop = ttk.Button(self.inputFrame, text='stop').grid(row =0, column = 1)
        self.reset = ttk.Button(self.inputFrame, text='reset').grid(row =0, column = 2)

        self.time = [minute, seconds]

    def chooseMinute(self):
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
    def chooseSeconds(self):
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

    def countdown(self, minute, seconds):
        self.timer['text'] = (self.minute, self.seconds)

        if self.minute == 0 and self.seconds == 0:
            sys.stdout.write("\r" + '{:02d}:{:02d}'.format(self.minute, self.seconds))
            return 0
        elif self.seconds == 0:
            sys.stdout.write("\r" + '{:02d}:{:02d}'.format(self.minute, self.seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = 60
            countdown(self.minute - 1, self.seconds - 1)
        else:
            sys.stdout.write("\r" + '{:02d}:{:02d}'.format(self.minute, self.seconds))
        sys.stdout.flush()
        time.sleep(1)
        countdown(self.minute, self.seconds - 1)




    def startButton(self):
        self.countdown(self.chooseMinute, self.chooseSeconds)

'''
    def stopButton(self):


    def resetButton(self):

#running the program.

print('Please enter a value for Minutes')
chooseMinute()

print('Please enter a value for Seconds')
chooseSeconds()
'''


def main():

    root = Tk()
    countdownTimerPage = countdownTimer(root)
    root.mainloop()


if __name__ == "__main__": main()
