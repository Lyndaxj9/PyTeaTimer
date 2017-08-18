#!/usr/local/bin/python3
import time
from threading import Thread

class CountdownTimer:
    def __init__(self):
        self.className = "CountdownTimer"
        #timer stored in seconds
        self.currentTimer = 0

    def printClassName(self):
        print(self.className)

    def countdown(self):
        t = self.currentTimer
        while( t > 0 ):
            print(self.convertToString(t), end='\r')
            time.sleep(1)
            t -= 1
        print("TEA IS READY!!!")

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
    ct.setTimerSecs(10)
    print(ct)
    ct.countdown()
