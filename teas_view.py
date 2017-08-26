#!/usr/local/bin/python3


class TeasView:
    def __init__(self):
        self.__title = " TEA VIEWER ".center(58, '=')
        self.__headerformat = "|{0:^3s}|{1:^25s}|{2:^8s}|{3:^8s}|{4:^8s}|"
        self.__teasformat = "|{0:^3d}|{1:^25s}|{2:^8s}|{3:^8d}|{4:^8s}|"
        self.headers = self.__headerformat.format('#', 'Name', 'Type', 'Temp', 'Time')
        self.__seperator = "=" * 58

        self.__prompt00 = "'S' to (S)elect a tea | 'B' to go (B)ack"
        self.__prompt01 = "'A' to view (A)ll teas"
        self.__prompt02 = "Enter the number for the tea you want to view: "
        self.__prompts = [self.__prompt00, self.__prompt01, self.__prompt02]

        self.__error00 = "ERROR: Please enter a valid command."
        self.__error01 = "ERROR: Number entered not within range."
        self.__errors = [self.__error00, self.__error01]

    def general_display(self):
        display = "%s\n%s\n%s" % (self.__title, self.headers, self.__prompt00)
        print(display)

    def prompt_display(self, in_promptnum):
        print(self.__prompts[in_promptnum])

    def error_display(self, in_errornum):
        print(self.__errors[in_errornum])

    def one_tea_display(self, in_tea):
        print(self.__title)
        print(in_tea)
        print(self.__seperator)
        print(self.__prompt01)

    def all_teas_display(self, all_teas):
        print("%s\n%s" % (self.__title, self.headers))
        for i, row in enumerate(all_teas):
            print(self.__teasformat.format(i+1, row[1], row[2], row[3], row[4]))
        print("%s\n%s" % (self.__seperator, self.__prompt00))
