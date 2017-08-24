#!/usr/local/bin/python3
import csv
""" Script that takes the info from a .csv file with a header 
and returns a list of tuples of the data from the .csv file
"""


def read_file(file_name):
    """ Reads data from .csv file skips the header and returns a list with all the data """
    alldata = []
    with open(file_name, newline='') as csvfile:
        filtered = (line.replace('\r', '\n') for line in csvfile)  # get rid of carriage return
        valuereader = csv.reader(filtered)
        next(valuereader, None)  # skip the header
        for row in valuereader:
            alldata.append(tuple(row))
    return alldata


def print_data(list_data):
    """ Prints data from list with each tuple in a new line"""
    for r in list_data:
        print(r)


if __name__ == '__main__':
    defaultfile = "teainfo.csv"
    filename = input("What is the file name?: ")

    if filename == "":
        filename = defaultfile
    newlist = read_file(filename)
    print_data(newlist)
