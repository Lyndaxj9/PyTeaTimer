#!/usr/local/bin/python3
from countdown_timer import CountdownTimer
from teas_controller import TeasController


def main():
    countdown = CountdownTimer()
    tea_ctrl_view = TeasController()

    print("Welcome to PyTea Timer")

    response = ''
    while response.upper() != 'Q':
        response = input("Would you like to? (V)iew Teas | (S)et Timer | (B)egin Timer | (Q)uit: ")
        if response.upper() == 'S':
            new_minutes = input("How many minutes?: ")
            new_seconds = input("How many seconds?: ")
            while not(countdown.set_timer_min_secs(new_minutes, new_seconds)):
                print("Please input integer values.")
                new_minutes = input("How many minutes?: ")
                new_seconds = input("How many seconds?: ")
        elif response.upper() == 'B':
            countdown.countdown()
        elif response.upper() == 'V':
            tea_ctrl_view.get_all_teas()
            view_response = ''
            while view_response.upper() != 'B':
                view_response = input()
                if view_response.upper() == 'S':
                    tea_ctrl_view.get_all_teas_select()
                    view_response = input()
                    if view_response.isdigit():
                        tea_ctrl_view.get_one_tea(view_response)
                elif view_response.upper() == 'A':
                    tea_ctrl_view.get_all_teas()
                elif view_response.upper() == 'B':
                    pass
                else:
                    tea_ctrl_view.get_all_teas()
                    tea_ctrl_view.tView.error_display(0)
        elif response.upper() == 'Q':
            print('Goodbye.')
        else:
            print('Response not recognized please try again.')

if __name__ == '__main__':
    main()
