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
        self.__edited_sect = -1

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

    def edit_one_data(self):
        self.tView.one_tea_edit_new_display(self.__teaholder, self.__edited_sect)

    def data_editor(self, section_num):
        """ Edit the data based on the section user chooses to modify. """
        section_num = int(section_num)
        if 1 <= section_num <= 10:
            a_tuple = self.__teaColumns[section_num-1]
            entered_data = self.tView.input_w_default(5, self.__teaholder[a_tuple[1]])  # 5 is a text prompt num
            newdata = self.data_verifier(section_num, entered_data)
            if newdata is not None:
                self.__teaholder[a_tuple[1]] = newdata
                self.__edited_sect = 1
            else:
                self.__edited_sect = 0

    def data_verifier(self, section_num, newdata):
        """ Check that the data entered for the section is valid. """
        validvalue = None
        section_selected = self.__teaColumns[section_num-1][0]

        if section_selected == "tea_name" or section_selected == "tea_type" or section_selected == "brand":
            validvalue = newdata
        elif section_selected == "temperature":
            if newdata.isdigit() and 35 <= int(newdata) <= 215:
                validvalue = int(newdata)
        elif section_selected == "package":
            ndatalower = newdata.lower()
            if ndatalower == "loose" or ndatalower == "bag" or ndatalower == "pyramid":
                validvalue = newdata.capitalize()
        elif section_selected == "time":
            timeparts = newdata.split(':')
            if len(timeparts) == 2:
                if timeparts[0].isdigit() and timeparts[1].isdigit() and \
                                len(timeparts[0]) <= 2 and len(timeparts[1]) <= 2:
                    mins = int(timeparts[0])
                    secs = int(timeparts[1])
                    if 0 <= mins <= 59 and 0 <= secs <= 59:
                        validvalue = "{0:02d}:{1:02d}".format(mins, secs)
        elif section_selected == "price":  # maybe allow entering "#" for a flat dollar amount
            priceparts = newdata.split('.')
            if len(priceparts) == 2:
                if priceparts[0].isdigit() and priceparts[1].isdigit() and len(priceparts[1]) <= 2:
                    dollar = int(priceparts[0])
                    cents = int(priceparts[1])
                    if dollar >= 0 and 0 <= cents <= 99:
                        validvalue = float('.'.join([str(dollar), str(cents)]))
        elif section_selected == "notes":
            validvalue = newdata
        elif section_selected == "buy_again" or section_selected == "on_hand":
            ndatalower = newdata.lower()
            if ndatalower == "no" or ndatalower == "yes" or ndatalower == "maybe":
                if not(ndatalower == "maybe" and section_selected == "on_hand"):
                    validvalue = newdata.capitalize()

        return validvalue

    def update_one_tea(self):
        return self.__tModel.set_one_tea(self.__teaColumns, self.__teaholder, self.singleTea[0])


if __name__ == '__main__':
    tC = TeasController()
