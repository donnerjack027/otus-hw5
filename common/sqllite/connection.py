#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import logging as log


def create_connection(db_file):
    """
    create a database connection to the SQLite database by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as connection_error:
        log.error(connection_error)
    return None


def input_logs__proxy(connection, proxy):
    """
    commit proxy logs to data base
    :param connection: db connection
    :param proxy: proxy logs
    """
    proxy_logs = proxy.har['log']
    cursor = connection.cursor()
    val = (str(proxy_logs['version']),
           str(proxy_logs['creator']),
           str(proxy_logs['pages']),
           str(proxy_logs['entries']),
           str(proxy_logs['comment']))
    cursor.execute('INSERT INTO proxy_logs VALUES (?, ?, ?, ?, ?)', val)
    connection.commit()
    cursor.close()


def main(proxy):
    database = "reports/log_base.db"
    connection = create_connection(database)
    with connection:
        log.info("writing logs into db")
        input_logs__proxy(connection, proxy)
    connection.close()
