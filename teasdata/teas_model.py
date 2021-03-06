#!/usr/local/bin/python3
from db_functions import *


class TeasModel:
    def __init__(self, inteas_db):
        """ Creates a connect to the database with the tea info. """
        self.__DBCONN = create_connection(inteas_db)
        self.databaseconnected = True
        self.allteas = []
        if self.__DBCONN is None:
            self.databaseconnected = False
            print("ERROR. Database connection not established.")

    def get_teas(self):
        """ Get all the teas in the database.
        Only the id, tea_name, tea_type, temperature, and time columns.
        """
        if self.databaseconnected:
            sql_select_all_teas = """ SELECT id, tea_name, tea_type, temperature, time FROM teas; """
            self.allteas = select_from_table(self.__DBCONN, sql_select_all_teas)
            return self.allteas
        else:
            print("No database connection exists.")

    def get_one_tea(self, tea_id):
        """ Get all information about a single tea in the database.
        Selected by its id number.
        """
        if self.databaseconnected:
            sql_select_one_tea = """ SELECT * FROM teas WHERE id = ?; """
            singletea = select_from_table_params(self.__DBCONN, sql_select_one_tea, [tea_id])
            return singletea
        else:
            print("No database connection exists.")

    def set_one_tea(self, tea_columns, tea_info, tea_id):
        """ Create query statement and update the columns of a single tea based on the
        information that was modified in the tuple list
        """
        query = ''' UPDATE teas SET '''
        items = []
        for col, idx in tea_columns:
            if tea_info[idx] != tea_id[idx]:
                if items == []:
                    items.append(tea_info[idx])
                    query = query + col + " = ?"
                else:
                    items.append(tea_info[idx])
                    query = query + ", " + col + " = ?"

        if items != []:
            items.append(tea_id[0])
            query = query + " WHERE id = ?"

        if self.databaseconnected:
            return update_row_in_table(self.__DBCONN, query, tuple(items))
        else:
            print("No database connection exists.")
            return False



if __name__ == '__main__':
    tm = TeasModel("tea.db")
    tm.get_teas()
