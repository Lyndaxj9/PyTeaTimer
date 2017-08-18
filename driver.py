#!/usr/local/bin/python3
from countdown_timer import CountdownTimer

def main():
    ct = CountdownTimer()
    minutes = input("enter mins: ")
    secs = input("enter secs: ")
    ct.setTimerMinSecs(minutes, secs)

    """
    th = Thread(target=timerapp, args=(brewTime,)) 
    th.start()
    
    at the moment doesn't work with threads need to handle that
    except KeyboardInterrupt:
        response = input("(Q)uit | (C)ancel timer")
        if response == "Q":
            sys.exit(0)
        elif response == "C":
            t.cancel()
    """
        

if __name__ == '__main__' : main()
