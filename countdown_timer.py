#!/usr/local/bin/python3
from threading import Thread

class CountdownTimer:
    def __init__(self):
        self.className = "CountdownTimer"
        self.currentTime = 0

    def printClassName(self):
        print(self.className)

    def getCurrentTime(self):
        return self.currentTime

        
if __name__ == '__main__':
    ct = CountdownTimer()
    ct.printClassName()
