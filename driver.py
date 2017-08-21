#!/usr/local/bin/python3
from countdown_timer import CountdownTimer


def main():
    ct = CountdownTimer()
    print("Welcome to PyTea Timer")

    response = ''
    while response != 'Q':
        response = input("Would you like to? (V)iew Teas | (S)et Timer | (B)egin Timer | (Q)uit: ")
        if response == 'S':
            new_minutes = input("How many minutes?: ")
            new_seconds = input("How many seconds?: ")
            while not(ct.set_timer_min_secs(new_minutes, new_seconds)):
                print("Please input integer values.")
                new_minutes = input("How many minutes?: ")
                new_seconds = input("How many seconds?: ")
        elif response == 'B':
            ct.countdown()
        elif response == 'V':
            print('View of all available teas and that interface (TBA)')
        elif response == 'Q':
            print('Goodbye.')
        else:
            print('Response not recognized please try again.')

if __name__ == '__main__':
    main()
