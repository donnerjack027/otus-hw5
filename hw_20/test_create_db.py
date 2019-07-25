#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from hw_20.db.connector import SqlTest


def test_create_db():
    db = SqlTest()
    connection = db.mysql_connect()
    db.create_table(connection)
    db.check_table(connection)
    db.remove_table(connection)
