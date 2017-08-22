#!/usr/local/bin/python3
import csv


def read_file(file_name):
    alldata = []
    with open(file_name, newline='') as csvfile:
        valuereader = csv.reader(csvfile)  # skip the header
        next(valuereader, None)
        for row in valuereader:
            alldata.append(tuple(row))
    return alldata


def print_data(list_data):
    for r in list_data:
        print(r)


if __name__ == '__main__':
    filename = input("What is the file name?: ")
    newlist = read_file(filename)
    print_data(newlist)
