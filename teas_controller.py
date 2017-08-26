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

    def get_all_teas_select(self):
        self.tView.all_teas_display(self.manyTea)
        self.tView.prompt_display(2)

    def get_one_tea(self, in_teaselect):
        in_teaselect = int(in_teaselect)-1
        if 0 <= in_teaselect < len(self.manyTea):
            self.singleTea = self.manyTea[in_teaselect]
            self.tView.one_tea_display(self.singleTea)
        else:
            self.tView.error_display(1)

if __name__ == '__main__':
    tC = TeasController()
