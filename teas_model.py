#!/usr/local/bin/python3
from db_functions import *


class TeasModel:
    def __init__(self, inteas_db):
        self.__DBCONN = create_connection(inteas_db)
