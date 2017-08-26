#!/usr/local/bin/python3
from teas_model import *
from teas_view import *


class TeasController:
    def __init__(self):
        self.__tModel = TeasModel("tea.db")
        self.__tView = TeasView()
        self.singleTea = ()
        self.manyTea = self.__tModel.get_teas()

    def get_all_teas(self):
        self.__tView.all_teas_display(self.manyTea)

    def display_teas(self):
        self.__tView.general_display()

if __name__ == '__main__':
    tC = TeasController()
    tC.display_teas()
    tC.get_all_teas()
