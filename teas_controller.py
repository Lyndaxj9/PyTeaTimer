#!/usr/local/bin/python3
from teas_model import *
from teas_view import *


class TeasController:
    def __init__(self):
        self.__tModel = TeasModel("tea.db")
        self.tView = TeasView()
        self.singleTea = ()
        self.manyTea = self.__tModel.get_teas()

    def get_all_teas(self):
        self.tView.all_teas_display(self.manyTea)

    def get_one_tea(self):
        self.tView.one_tea_display()

if __name__ == '__main__':
    tC = TeasController()
