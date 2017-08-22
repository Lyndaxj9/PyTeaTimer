#!/usr/local/bin/python3
import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    database = "tea.db"

    sql_create_tea_table = """ CREATE TABLE IF NOT EXISTS teas (
                                    id integer PRIMARY KEY NOT NULL,
                                    tea_name character NOT NULL,
                                    temperature DECIMAL(6,3) NOT NULL,
                                    time text NOT NULL,
                                    notes text,
                                    package character,
                                    brand character,
                                    buy_again character,
                                    on_hand boolean,
                                    price DECIMAL(6,3)
                                    ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_tea_table)
    else:
        print("Error! cannot create the database connection.")
