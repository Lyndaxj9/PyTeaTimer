#!/usr/local/bin/python3


class TeasView:
    def __init__(self):
        """ Create all the text that will be needed to present tea information. """
        self.__degreesign = u'\N{DEGREE SIGN}'

        self.__title = " TEA VIEWER ".center(58, '=')
        self.__headerformat = "|{0:^3s}|{1:^25s}|{2:^8s}|{3:^8s}|{4:^8s}|"
        self.__teasformat = "|{0:^3d}|{1:^25s}|{2:^8s}|{3:^8d}|{4:^8s}|"
        self.__headers = self.__headerformat.format('#', 'Name', 'Type', 'Temp'+self.__degreesign+'F', 'Time')
        self.__seperator = "=" * 58

        self.__namebrandformat = "|{0:24s} ({2:^8s})|Brand: {1:13s}|"
        self.__temppkgformat = "|{0:<35s}|Packaging: {1:9s}|"
        self.__timepriceformat = "|{0:02d}:{1:02d} {3:29s}|Price:${2:3.2f}|"

        self.__prompt00 = "'S' to (S)elect a tea | 'B' to go (B)ack"
        self.__prompt01 = "'A' to view (A)ll teas"
        self.__prompt02 = "Enter the number for the tea you want to view: "
        self.__prompts = [self.__prompt00, self.__prompt01, self.__prompt02]

        self.__error00 = "ERROR: Please enter a valid command."
        self.__error01 = "ERROR: Number entered not within range."
        self.__error02 = "ERROR: Tea could not be found in database."
        self.__errors = [self.__error00, self.__error01, self.__error02]

    def general_display(self):
        display = "%s\n%s\n%s" % (self.__title, self.__headers, self.__prompt00)
        print(display)

    def prompt_display(self, in_promptnum):
        """ Prints one of the prompts selected by the in_promptnum param. """
        print(self.__prompts[in_promptnum])

    def error_display(self, in_errornum):
        """ Prints one of the errors selected by the in_errornum param. """
        print(self.__errors[in_errornum])

    # TODO better format price print
    def one_tea_display(self, in_tea):
        """ Print information about one tea that is passed in. """
        in_tea = in_tea[0]
        temp = str(in_tea[3]) + self.__degreesign + "F"
        timeparts = in_tea[4].split(':')
        # if(in_tea[10])
        print(self.__title)
        print(self.__namebrandformat.format(in_tea[1], in_tea[7], in_tea[2]))
        print(self.__temppkgformat.format(temp, in_tea[6]))
        print(self.__timepriceformat.format(int(timeparts[0]), int(timeparts[1]), in_tea[10], "mins"))
        print(in_tea)
        print(self.__seperator)
        print(self.__prompt01)

    def all_teas_display(self, all_teas):
        """ Print general information about all the teas in the all_teas param list. """
        print("%s\n%s" % (self.__title, self.__headers))
        for i, row in enumerate(all_teas):
            print(self.__teasformat.format(i+1, row[1], row[2], row[3], row[4]))
        print(self.__seperator)
