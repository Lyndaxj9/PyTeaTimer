#!/usr/local/bin/python3
from teasdata.teas_model import *
from teasdata.teas_view import *


class TeasController:
    def __init__(self):
        """ Create a connection to the teas_model and teas_view. """
        self.__tModel = TeasModel("teasdata/tea.db")
        self.tView = TeasView()
        self.singleTea = ()
        self.__teaholder = []
        self.__teaColumns = (("tea_name", 1), ("tea_type", 2), ("brand", 7), ("temperature", 3), ("package", 6),
                             ("time", 4), ("price", 10), ("notes", 5), ("buy_again", 8), ("on_hand", 9))
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
                self.__teaholder = list(self.singleTea[0])
                self.tView.one_tea_display(self.singleTea, in_status)
            else:
                self.get_all_teas()
                self.tView.error_display(2)
        else:
            self.tView.error_display(1)
            self.tView.prompt_display(0)

    def set_tea_timer(self):
        """ Takes the current single tea on display and returns the min and secs so that the countdown timer
        can be set
        """
        teatime = self.singleTea[0][4]
        timenumbers = teatime.split(':')

        return timenumbers[0], timenumbers[1]

    # TODO add functionality to edit tea information
    def edit_one_tea(self):
        self.tView.one_tea_edit_new_display(self.__teaholder)
        # print(self.singleTea)
        # self.tView.one_tea_display(self.singleTea, False)

    def data_editor(self, section_num):
        """ Edit the data based on the section user chooses to modify. """
        section_num = int(section_num)
        if 1 <= section_num <= 10:
            a_tuple = self.__teaColumns[section_num-1]
            print(self.__teaholder)
            entered_data = self.tView.input_w_default(5, self.__teaholder[a_tuple[1]])
            newdata = self.data_verifier(section_num, entered_data)
            if newdata is not None:
                self.__teaholder[a_tuple[1]] = newdata
            print(newdata)

    def data_verifier(self, section_num, newdata):
        """ Check that the data entered for the section is valid. """
        validvalue = None
        if self.__teaColumns[section_num-1][0] == "temperature":  # temperature
            if newdata.isdigit() and 35 <= int(newdata) <= 215:
                validvalue = int(newdata)
                print(True)

        return validvalue


if __name__ == '__main__':
    tC = TeasController()
