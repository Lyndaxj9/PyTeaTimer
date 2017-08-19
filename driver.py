#!/usr/local/bin/python3
from countdown_timer import CountdownTimer

def main():
    ct = CountdownTimer()
    minutes = input("enter mins: ")
    secs = input("enter secs: ")
    ct.setTimerMinSecs(minutes, secs)

if __name__ == '__main__' : main()
