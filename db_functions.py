#!/usr/local/bin/python3
import sqlite3
""" A script to create/connect to a database, create tables, and insert data"""


def create_connection(db_file):
    """ Create a connection to the database passed and return it.
    Return none if it could not be connected to.
    """
    try:
        in_conn = sqlite3.connect(db_file)
        return in_conn
    except sqlite3.Error as e:
        print(e)

    return None


def create_table(in_conn, create_table_sql):
    """ Create a table in the passed database. """
    try:
        c = in_conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_data_many(in_conn, insert_data_query, insert_data_list):
    """ Insert multiple rows of data using the query and list passed. """
    try:
        c = in_conn.cursor()
        c.executemany(insert_data_query, insert_data_list)
    except sqlite3.Error as e:
        print(e)


def select_from_table(in_conn, select_query):
    """ Select rows from table using the query passed and return a list """
    try:
        c = in_conn.cursor()
        c.execute(select_query)

        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)


def select_from_table_params(in_conn, select_query, paramvars):
    """ Select rows from table using the query and var params for (?), return a list """
    try:
        c = in_conn.cursor()
        c.execute(select_query, paramvars)

        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)

def update_row_in_table(in_conn, update_query, paramvars):
    try:
        c = in_conn.cursor()
        c.execute(update_query, paramvars)
        in_conn.commit()
        print("update made!")
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    database = "teasdata/tea.db"

    conn = create_connection(database)
    if conn is not None:
        print("Hurray! created the database connection.")
        query = ''' UPDATE teas SET notes = ?, price = ? WHERE id = ?'''
        tasks = ("wow this tea pretty alright!", 4.00, 4)
        update_row_in_table(conn, query, tasks)
    else:
        print("Error! cannot create the database connection.")

    conn.close()
