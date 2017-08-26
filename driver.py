#!/usr/local/bin/python3
from countdown_timer import CountdownTimer
from teas_controller import TeasController


def main():
    countdown = CountdownTimer()
    tea_ctrl_view = TeasController()

    print("Welcome to PyTea Timer")

    response = ''
    while response != 'Q':
        response = input("Would you like to? (V)iew Teas | (S)et Timer | (B)egin Timer | (Q)uit: ")
        if response == 'S':
            new_minutes = input("How many minutes?: ")
            new_seconds = input("How many seconds?: ")
            while not(countdown.set_timer_min_secs(new_minutes, new_seconds)):
                print("Please input integer values.")
                new_minutes = input("How many minutes?: ")
                new_seconds = input("How many seconds?: ")
        elif response == 'B':
            countdown.countdown()
        elif response == 'V':
            tea_ctrl_view.get_all_teas()
            view_response = ''
            while view_response != 'B':
                view_response = input()
                if view_response == 'S':
                    tea_ctrl_view.get_one_tea()
                elif view_response == 'A':
                    tea_ctrl_view.get_all_teas()
                elif view_response == 'B':
                    pass
                else:
                    tea_ctrl_view.get_all_teas()
                    print("Please enter a valid command.")
        elif response == 'Q':
            print('Goodbye.')
        else:
            print('Response not recognized please try again.')

if __name__ == '__main__':
    main()
