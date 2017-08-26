#!/usr/local/bin/python3
from db_functions import *


class TeasModel:
    def __init__(self, inteas_db):
        self.__DBCONN = create_connection(inteas_db)
        self.databaseconnected = True
        self.allteas = []
        if self.__DBCONN is None:
            self.databaseconnected = False
            print("ERROR. Database connection not established.")

    def get_teas(self):
        if self.databaseconnected:
            sql_select_all_teas = """ SELECT id, tea_name, tea_type, temperature, time FROM teas; """
            self.allteas = select_from_table(self.__DBCONN, sql_select_all_teas)
            return self.allteas
        else:
            print("No database connection exists.")

    def get_one_tea(self, tea_id):
        if self.databaseconnected:
            sql_select_one_tea = """ SELECT * FROM teas WHERE id = ?; """
            singletea = select_from_table_params(self.__DBCONN, sql_select_one_tea, [tea_id])
            return singletea
        else:
            print("No database connection exists.")

if __name__ == '__main__':
    tm = TeasModel("tea.db")
    tm.get_teas()
