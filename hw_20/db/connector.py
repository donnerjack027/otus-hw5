#!/usr/bin/python

from mysql.connector import connection
import logging as log


class SqlTest:
    def __init__(self):
        self.config = {'user': 'ocuser',
                       'password': 'PASSWORD',
                       'host': '127.0.0.1',
                       'database': 'opencart',
                       'raise_on_warnings': True}
        self.table_name = 'test'

    def mysql_connect(self):
        connect = connection.MySQLConnection(**self.config)
        return connect

    def create_table(self, connect):
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE {} (id INT, name VARCHAR(20))".format(self.table_name))
        connect.commit()
        cursor.close()

    def remove_table(self, connect):
        cursor = connect.cursor()
        cursor.execute("DROP TABLE {}".format(self.table_name))
        connect.commit()
        cursor.close()

    def check_table(self, connect):
        cursor = connect.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        try:
            self.table_name in tables
        except Exception:
            log.error("There are no table with name {}".format(self.table_name))
        cursor.close()
