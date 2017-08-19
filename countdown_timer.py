#!/usr/local/bin/python3
import time
import subprocess
import sys

class CountdownTimer:
    def __init__(self):
        self.className = "CountdownTimer"
        #timer stored in seconds
        self.currentTimer = 0
        self.audioFile = "Music_Box-Big_Daddy.wav"

    def printClassName(self):
        print(self.className)

    def countdown(self):
        t = self.currentTimer

        while( t > 0 ):
            #self.playsound()
            sys.stdout.write('\r' + self.convertToString(t))
            time.sleep(1)
            t -= 1

        sys.stdout.write('\r' + "TEA IS READY!!!" + '\n')

        '''
        except KeyboardInterrupt:
            response = input("(Q)uit | (C)ancel Timer")
            if(response == 'Q'):
                sys.exit(0)
            elif(response == 'C'):
                t = self.currentTimer
        '''

    def playsound(self):
        return_code = subprocess.call(["afplay", self.audioFile])


    def getTimerSecs(self):
        return self.currentTimer

    def setTimerSecs(self, seconds):
        self.currentTimer = seconds

    def setTimerMinSecs(self, minutes, seconds):
        self.currentTimer = minutes * 60 + seconds

    def convertToString(self, inTime = None):
        if (inTime is None):
            inTime = self.currentTimer
        minutes = int(inTime / 60)
        seconds = inTime% 60
        timeString = '{:02d}:{:02d}'.format(minutes, seconds)
        return timeString

    def __str__(self):
        outputTime = self.convertToString()
        return outputTime

if __name__ == '__main__':
    ct = CountdownTimer()
    ct.printClassName()
    ct.setTimerSecs(190)
    print(ct)
    ct.setTimerSecs(5)
    print(ct)
    ct.countdown()
