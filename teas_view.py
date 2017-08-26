#!/usr/local/bin/python3


class TeasView:
    def __init__(self):
        self.title = " TEA VIEWER ".center(58, '=')
        self.__headerformat = "|{0:^3s}|{1:^25s}|{2:^8s}|{3:^8s}|{4:^8s}|"
        self.__teasformat = "|{0:^3d}|{1:^25s}|{2:^8s}|{3:^8d}|{4:^8s}|"
        self.headers = self.__headerformat.format('#', 'Name', 'Type', 'Temp', 'Time')
        self.prompt = "'S' to (S)elect a tea\n'B' to go (B)ack"

    def general_display(self):
        display = "%s\n%s\n%s" % (self.title, self.headers, self.prompt)
        print(display)

    def prompt_display(self):
        print(self.prompt)

    def all_teas_display(self, all_teas):
        print("%s\n%s" % (self.title, self.headers))
        for row in all_teas:
            print(self.__teasformat.format(row[0], row[1], row[2], row[3], row[4]))
