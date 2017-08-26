#!/usr/local/bin/python3
from teas_model import *
from teas_view import *


class TeasController:
    def __init__(self):
        self.__tModel = TeasModel("tea.db")
        self.__tView = TeasView()
        self.__running = False
        self.singleTea = ()
        self.manyTea = self.__tModel.get_teas()

    def get_all_teas(self):
        self.__tView.all_teas_display(self.manyTea)

    def get_running(self):
        return self.__running

    def tea_control_loop(self):
        self.get_all_teas()
        self.__running = True
        response = ''
        while response != 'B':
            self.__tView.prompt_display()
            response = input()
            if response == 'S':
                print("Display one tea")
            elif response == 'B':
                self.__running = False
            else:
                print("Please enter a valid command.")

if __name__ == '__main__':
    tC = TeasController()
    tC.tea_control_loop()
