import datetime
import mysql.connector
import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder


class MySQLDatabase():

    def __init__(self):

        self.ssh_host = '20.5.240.150'
        self.ssh_port = 22
        self.ssh_username = 'azureuser'
        self.ssh_password = 'fit5120'
        self.ssh_pkey_file = "C:/Users/liyon/Desktop/2023S1/FIT5120/migrantworkersprotector-main" \
                             "/migrantworkersprotector/fit5120tp09au_key.pem "

        self.database_host = '20.5.240.150'
        self.database_port = 3306
        self.database_username = 'developer'
        self.database_name = 'worker'
        self.database_password = 'fit5120'

        self.server = None
        self.conn = None
        self.cursor = None

    def connect(self, verbose=False):
        """Open an SSH tunnel and connect using a username and password.
            Connect to a MySQL server using the SSH tunnel connection

            :param verbose: Set to True to show logging
            :return tunnel: Global SSH tunnel connection
            :return connection: Global MySQL database connection
           """

        # if verbose:
        #     sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
        #
        # self.server = SSHTunnelForwarder(
        #     (self.ssh_host, 22),
        #     ssh_username=self.ssh_username,
        #     ssh_password=self.ssh_password,
        #     ssh_pkey=self.ssh_pkey_file,
        #     remote_bind_address=(self.database_host, self.database_port)
        # )
        #
        # self.server.start()

        try:
            self.conn = mysql.connector.connect(host=self.database_host,
                                                port=self.database_port,
                                                user=self.database_username,
                                                password=self.database_password,
                                                database=self.database_name
                                                )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(err)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def tables_setup(self):

        sql_cmd1 = """CREATE TABLE IF NOT EXISTS BackgroundInfo(
                    info_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    age varchar(3),
                    gender varchar(100),
                    major varchar(100) NOT NULL,
                    skills varchar(100) NOT NULL,
                    industry varchar(100),
                    experience varchar(700) NOT NULL
                    )"""

        self.cursor.execute(sql_cmd1)
        self.commit()

    def add_info(self, age, gender, major, skills, industry, experience):

        sql_cmd = """INSERT INTO BackgroundInfo(age, gender, major, skills, industry, experience)
                        VALUES('{age}', '{gender}','{major}', '{skills}', '{industry}', "{experience}")
                        """.format(age=age, gender=gender, major=major, skills=skills, industry=industry, experience=experience)
        self.cursor.execute(sql_cmd)

        self.commit()

        return True

    #
    def get_allInfos(self):
        sql_cmd = """SELECT *
                FROM BackgroundInfo
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        # print(result)
        self.commit()

        return result

    # def get_searchEvent(self, search_keywords):
    #     sql_cmd = """SELECT *
    #                     FROM Events
    #                     WHERE event_topic LIKE '%{event_topic}%'
    #                     ORDER BY event_time DESC
    #                     """.format(event_topic=search_keywords)
    #
    #     self.cursor.execute(sql_cmd)
    #
    #     result = list(self.cursor.fetchall())
    #     # print(result)
    #     self.commit()
    #
    #     return result
    #
    #     # function used to get the data in recycle_area, and display in the wastemap page
    #
    # def get_allArea(self):
    #     sql_cmd = """
    #                SELECT * FROM recycle_area
    #                """
    #
    #     self.cursor.execute(sql_cmd)
    #     result = list(self.cursor.fetchall())
    #     # print(result)
    #     self.commit()
    #
    #     return result
    #
    # def get_searchLocation(self, search_keywords):
    #     sql_cmd = """SELECT *
    #                             FROM recycle_area
    #                             WHERE Local_Government LIKE '%{Local_Government}%'
    #                             """.format(Local_Government=search_keywords)
    #
    #     self.cursor.execute(sql_cmd)
    #
    #     result = list(self.cursor.fetchall())
    #     # print(result)
    #
    #     self.commit()
    #
    #     # print("database")
    #     return result
    #
    # def get_searchWaste(self, search_keywords):
    #     sql_cmd = """SELECT *
    #                 FROM recycle_bins_items
    #                 WHERE items LIKE '%{items}%'
    #             """.format(items=search_keywords)
    #
    #     self.cursor.execute(sql_cmd)
    #
    #     result = list(self.cursor.fetchall())
    #     print(result)
    #
    #     self.commit()
    #
    #     # print("database")
    #     return result
