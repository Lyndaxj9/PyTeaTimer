#!/usr/local/bin/python3
import sys
from threading import Timer

def timerapp():
    print("timer app")

def main():
    minutes = input("enter mins: ")
    secs = input("enter secs: ")
    brewTime = int(minutes)*60 + int(secs)

    t = Timer(brewTime, timerapp)
    t.start()
    
    """
    at the moment doesn't work with threads need to handle that
    except KeyboardInterrupt:
        response = input("(Q)uit | (C)ancel timer")
        if response == "Q":
            sys.exit(0)
        elif response == "C":
            t.cancel()
    """
        

if __name__ == '__main__' : main()
