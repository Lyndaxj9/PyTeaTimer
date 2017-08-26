#!/usr/local/bin/python3
from csv_reader import *
from db_functions import *


if __name__ == '__main__':
    teainfo = read_file("teainfo.csv")
    database = "tea.db"

    sql_create_tea_table = """ CREATE TABLE IF NOT EXISTS teas (
                                        id integer PRIMARY KEY NOT NULL,
                                        tea_name character NOT NULL,
                                        tea_type character NOT NULL,
                                        temperature DECIMAL(6,3) NOT NULL,
                                        time text NOT NULL,
                                        notes text,
                                        package character,
                                        brand character,
                                        buy_again character,
                                        on_hand boolean,
                                        price DECIMAL(6,3)
                                        ); """

    sql_insert_tea_table = """ INSERT INTO teas('tea_name', 'tea_type', 'temperature', 'time', 'notes', 'package', 
                            'brand', 'buy_again', 'on_hand', 'price') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_tea_table)
        # at the moment the data from the csv will swap teaname and teatype
        insert_data_many(conn, sql_insert_tea_table, teainfo)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

    conn.close()
