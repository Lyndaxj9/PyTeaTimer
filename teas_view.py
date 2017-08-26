#!/usr/local/bin/python3


class TeasView:
    def __init__(self):
        self.__title = " TEA VIEWER ".center(58, '=')
        self.__headerformat = "|{0:^3s}|{1:^25s}|{2:^8s}|{3:^8s}|{4:^8s}|"
        self.__teasformat = "|{0:^3d}|{1:^25s}|{2:^8s}|{3:^8d}|{4:^8s}|"
        self.headers = self.__headerformat.format('#', 'Name', 'Type', 'Temp', 'Time')
        self.__seperator = "=" * 58
        self.__prompt01 = "'S' to (S)elect a tea | 'B' to go (B)ack"
        self.__prompt02 = "'A' to view (A)ll teas"

    def general_display(self):
        display = "%s\n%s\n%s" % (self.__title, self.headers, self.__prompt01)
        print(display)

    def prompt_display(self):
        print(self.__prompt01)

    def one_tea_display(self):
        print(self.__title)
        print("Display one tea info\n%s" % self.__seperator)
        print(self.__prompt02)

    def all_teas_display(self, all_teas):
        print("%s\n%s" % (self.__title, self.headers))
        for i, row in enumerate(all_teas):
            print(self.__teasformat.format(i, row[1], row[2], row[3], row[4]))
        print("%s\n%s" % (self.__seperator, self.__prompt01))
