#!/usr/local/bin/python3
import sys
import time
from threading import Timer
from threading import Thread

def timerapp(t):
    while t > 0:
        print(t, end='\r')
        time.sleep(1)
        t -= 1
    print("timer app")

def main():
    minutes = input("enter mins: ")
    secs = input("enter secs: ")
    brewTime = int(minutes)*60 + int(secs)

    th = Thread(target=timerapp, args=(brewTime,)) 
    th.start()
    
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
