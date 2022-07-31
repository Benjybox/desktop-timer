import time
import datetime
# This is a class that acts as a countdown timer. Create inputs in the program for hours, minutes, seconds and plug those into countdown_timer(h, m, s), or state them yourself if you want to be in control!


def countdown_timer(h, m, s):

    seconds_left = h * 3600 + m * 60 + s

    while seconds_left > 0:
        
        timer = datetime.timedelta(seconds = seconds_left)
        print(timer, end="\r")

        time.sleep(1)

        seconds_left -= 1

    print('BOOOONG!!!')

countdown_timer(0, 0, 15)