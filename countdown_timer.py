#!/usr/local/bin/python3
import time
import subprocess
import sys


class CountdownTimer:
    """ Countdown Timer is a class that creates a timer that will countdown from any number
    put into it from at most 99min 60sec
    The minutes and seconds counted down are displayed and a sound emits on the completion of the timer
    """

    def __init__(self):
        """Creates a timer object with a default current time and audio file
        currentTime is stored in seconds
        """
        self.currentTimer = 0
        self.__MAX_TIME = 6000
        self.audioFile = "sounds/Music_Box-Big_Daddy.wav"

    def countdown(self):
        """A method that runs for currentTimer time displaying how much time is left
        then indicates to user when the countdown is over with text and a sound
        """
        if self.currentTimer != 0:
            t = self.currentTimer

            while t > 0:
                sys.stdout.write('\r' + self.convert_to_string(t))
                time.sleep(1)
                t -= 1

            sys.stdout.write('\r' + "TEA IS READY!!!" + '\n')
            # self.play_sound()
        else:
            print("Please set the timer.")
            return False

        '''
        except KeyboardInterrupt:
            response = input("(Q)uit | (C)ancel Timer")
            if(response == 'Q'):
                sys.exit(0)
            elif(response == 'C'):
                t = self.currentTimer
        '''

    # TODO take care of return_code from the subprocess call
    def play_sound(self):
        """Plays a sound (on Mac) using the terminal audio player and a subprocess"""
        return_code = subprocess.call(["afplay", self.audioFile])

    def get_timer_secs(self):
        """Returns the current timer in seconds (int)"""
        return self.currentTimer

    def __check_time_set(self, seconds):
        # check if the numbers are integers
        return seconds <= self.__MAX_TIME

    # TODO add function to check if set_timer_* inputs are valid
    def set_timer_secs(self, seconds):
        """Sets currentTimer taking in a seconds format"""
        if self.__check_time_set(seconds):
            self.currentTimer = seconds
            return True
        else:
            return False

    def set_timer_min_secs(self, minutes, seconds):
        """Sets currentTimer taking in a minutes seconds format"""
        seconds_time = minutes * 60 + seconds
        return self.set_timer_secs(seconds_time)

    def convert_to_string(self, in_time=None):
        """Converts the int currentTimer that is in seconds to be displayed in min:sec format {00:00}"""
        if in_time is None:
            in_time = self.currentTimer
        minutes = int(in_time / 60)
        seconds = in_time % 60
        time_string = '{:02d}:{:02d}'.format(minutes, seconds)
        return time_string

    def __str__(self):
        output_time = self.convert_to_string()
        return output_time

if __name__ == '__main__':
    ct = CountdownTimer()
    ct.set_timer_secs(190)
    print(ct)
    ct.set_timer_secs(5)
    print(ct)
    ct.countdown()
