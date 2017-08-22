#!/usr/local/bin/python3
import sqlite3


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


def insert_data(in_conn, insert_data_query, insert_data_list):
    try:
        c = in_conn.cursor()
        c.executemany("""INSERT INTO teas('tea_name', 'tea_type', 'temperature', 'time', 'notes', 'package', 
                            'brand', 'buy_again', 'on_hand', 'price') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", insert_data_list)
    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    database = "tea.db"

    conn = create_connection(database)
    if conn is not None:
        print("Hurray! created the database connection.")
    else:
        print("Error! cannot create the database connection.")

    conn.close()
