#!/usr/local/bin/python3
from teasdata.teas_model import *
from teasdata.teas_view import *


class TeasController:
    def __init__(self):
        """ Create a connection to the teas_model and teas_view. """
        self.__tModel = TeasModel("teasdata/tea.db")
        self.tView = TeasView()
        self.singleTea = ()
        self.manyTea = self.__tModel.get_teas()

    def get_all_teas(self):
        """ Gets all the teas as a list from model and display it via view.
        Display prompt asking to if want to select tea.
        """
        self.tView.all_teas_display(self.manyTea)
        self.tView.prompt_display(0)

    def get_all_teas_select(self):
        """ Gets all the teas as a list from model and display it via view.
        Display prompt to select tea by number.
        """
        self.tView.all_teas_display(self.manyTea)
        self.tView.prompt_display(2)

    def get_one_tea(self, in_teaselect, in_status=-1):
        """ Attempt to retrieve and display info about a single selected tea. """
        in_teaselect = int(in_teaselect)-1
        if self.manyTea is not None and 0 <= in_teaselect < len(self.manyTea):
            singletea_id = self.manyTea[in_teaselect][0]
            self.singleTea = self.__tModel.get_one_tea(str(singletea_id))
            if self.singleTea is not None:
                self.tView.one_tea_display(self.singleTea, in_status)
            else:
                self.get_all_teas()
                self.tView.error_display(2)
        else:
            self.tView.error_display(1)
            self.tView.prompt_display(0)

    def set_tea_timer(self):
        """ Takes the current single tea on display and sets the countdown timer for this tea. """
        teatime = self.singleTea[0][4]
        timenumbers = teatime.split(':')

        return timenumbers[0], timenumbers[1]

    def update_one_tea(self):
        print("edit this tea")
        self.tView.one_tea_display(self.singleTea, False)

if __name__ == '__main__':
    tC = TeasController()
