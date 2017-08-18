#!/usr/local/bin/python3
from threading import Thread

class CountdownTimer:
    def __init__(self):
        self.className = "CountdownTimer"
        #timer stored in seconds
        self.currentTimer = 0

    def printClassName(self):
        print(self.className)

    def countdown(self):
        pass

    def getTimerSecs(self):
        return self.currentTimer

    def setTimerSecs(self, seconds):
        self.currentTimer = seconds

    def setTimerMinSecs(self, minutes, seconds):
        self.currentTimer = minutes * 60 + seconds

    def __str__(self):
        minutes = int(self.currentTimer / 60)
        seconds = self.currentTimer % 60
        outputTime = '{:02d}:{:02d}'.format(minutes, seconds)
        return outputTime

if __name__ == '__main__':
    ct = CountdownTimer()
    ct.printClassName()
    ct.setTimerSecs(190)
    print(ct)
