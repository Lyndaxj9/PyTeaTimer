#!/usr/local/bin/python3
from math import ceil


class TeasView:
    def __init__(self):
        """ Create all the text that will be needed to present tea information. """
        self.__degreesign = u'\N{DEGREE SIGN}'

        self.__title = " TEA VIEWER ".center(58, '=')
        self.__headerformat = "|{0:^3s}|{1:^25s}|{2:^8s}|{3:^8s}|{4:^8s}|"
        self.__teasformat = "|{0:^3d}|{1:^25s}|{2:^8s}|{3:^8d}|{4:^8s}|"
        self.__headers = self.__headerformat.format('#', 'Name', 'Type', 'Temp'+self.__degreesign+'F', 'Time')
        self.__seperator00 = "=" * 58
        self.__seperator01 = "-" * 58

        self.__namebrandformat = "|{0:24s} ({2:^8s})|Brand: {1:13s}|"
        self.__temppkgformat = "|{0:<35s}|Packaging: {1:9s}|"
        self.__timepriceformat = "|{0:02d}:{1:02d} {3:29s}|Price: ${2:3.2f}{4:>9}"
        self.__timepriceformat01 = "|{0:02d}:{1:02d} {3:29s}|Price: ${2:^12s}|"
        self.__notelinelen = 49
        self.__notesformat00 = "|Notes: {0:49s}|"
        self.__notesformat01 = "|{0:56s}|"
        self.__buyhandformat = "|Buy Again: {0:24s}|On Hand: {1:11s}|"

        self.__prompt00 = "'S' to (S)elect a tea | 'B' to go (B)ack"
        self.__prompt01 = "'A' to view (A)ll teas | 'T' to set (T)imer for this tea" \
                          "\n'E' to (E)dit tea information"
        self.__prompt02 = "Enter the number for the tea you want to view: "
        self.__prompts = [self.__prompt00, self.__prompt01, self.__prompt02]

        self.__error00 = "ERROR: Please enter a valid command."
        self.__error01 = "ERROR: Number entered not within range."
        self.__error02 = "ERROR: Tea(s) could not be found in database."
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

    def notes_printer(self, tea_notes):
        notelines = tea_notes.split('\n')
        print(self.__notesformat00.format(notelines[0][0:self.__notelinelen]))
        self.line_wrapper(notelines[0])
        if len(notelines) > 1:
            for i in range(1, len(notelines)):
                print(self.__notesformat01.format(notelines[i]))

    # TODO come up with better formula to split long string
    def line_wrapper(self, note_line):
        if len(note_line) > self.__notelinelen:
            lines = ceil(len(note_line) / self.__notelinelen)
            for i in range(1, int(lines)):
                print(self.__notesformat01.format(
                    note_line[i*self.__notelinelen:i*self.__notelinelen+self.__notelinelen]))

    def one_tea_display(self, in_tea):
        """ Print information about one tea that is passed in. """
        in_tea = in_tea[0]
        temp = str(in_tea[3]) + self.__degreesign + "F"
        timeparts = in_tea[4].split(':')
        # if(in_tea[10])
        print(self.__title)
        print(self.__namebrandformat.format(in_tea[1], in_tea[7], in_tea[2]))
        print(self.__temppkgformat.format(temp, in_tea[6]))
        if in_tea[10] != '':
            print(self.__timepriceformat.format(int(timeparts[0]), int(timeparts[1]), in_tea[10], "mins", "|"))
        else:
            print(self.__timepriceformat01.format(int(timeparts[0]), int(timeparts[1]), "-", "mins"))
        print(self.__seperator01)
        self.notes_printer(in_tea[5])
        print(self.__buyhandformat.format(in_tea[8], in_tea[9]))
        print(self.__seperator00)
        print(self.__prompt01)

    def all_teas_display(self, all_teas):
        """ Print general information about all the teas in the all_teas param list. """
        print("%s\n%s" % (self.__title, self.__headers))
        if all_teas is not None:
            for i, row in enumerate(all_teas):
                print(self.__teasformat.format(i+1, row[1], row[2], row[3], row[4]))
            print(self.__seperator00)
        else:
            print(self.__error02)

    def one_tea_timer(self, in_tea):
        print("timer set")
        self.one_tea_display(in_tea)
