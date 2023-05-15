import datetime
import mysql.connector
import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


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
        print("Start")
        try:
            self.conn = mysql.connector.connect(host=self.database_host,
                                                port=self.database_port,
                                                user=self.database_username,
                                                password=self.database_password,
                                                database=self.database_name
                                                )
            self.cursor = self.conn.cursor()
            print("Successful")
        except mysql.connector.Error as err:
            print("err")

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_allInfos_Calculator_Classification(self):
        sql_cmd = """SELECT DISTINCT Classification
                FROM Hour_pay_rate_FP_C
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        self.commit()
        # self.close()

        return result

    def get_allInfos_Calculator_Type(self):
        sql_cmd = """SELECT DISTINCT type
                FROM Hour_pay_rate_FP_C
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        self.commit()
        # self.close()

        return result

    def get_allInfos_AskForHelp_Type(self):
        sql_cmd = """SELECT DISTINCT type
                FROM AskForHelp
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        self.commit()
        # self.close()

        return result

    def get_allInfos_AskForHelp_Topic(self, quiz_type):
        sql_cmd = """SELECT DISTINCT topic
                FROM AskForHelp
                WHERE type LIKE '%{quiz_type}%'
                            """.format(quiz_type=quiz_type)

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        self.commit()
        # self.close()
        return result

    def get_allInfos_AskForHelp_Result(self, quiz_type, quiz_topic):
        sql_cmd = """SELECT description, ways
                FROM AskForHelp
                WHERE type LIKE '%{type}%' and topic LIKE '%{topic}%'
                            """.format(type=quiz_type, topic=quiz_topic)

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        self.commit()
        # self.close()

        return result


    def get_allInfos_WorkingRights(self):
        sql_cmd = """SELECT *
                FROM WorkingRightsWithID
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        # print(result)
        self.commit()
        # self.close()

        return result

    def get_allInfos_WorkingRights_Type(self):
        sql_cmd = """SELECT DISTINCT type
                FROM WorkingRightsWithID
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        # print(result)
        self.commit()
        # self.close()

        return result

    def get_allInfos_WorkingRights_Title(self):
        sql_cmd = """SELECT DISTINCT title
                FROM WorkingRightsWithID
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        # print(result)
        self.commit()
        # self.close()
        return result

    def get_searchGuideline(self, search_keywords):
        sql_cmd = """SELECT *
                        FROM WorkingRightsWithID
                        WHERE title LIKE '%{title}%' OR sub_title LIKE '%{sub_title}%' OR text_contents LIKE '%{text_contents}%'
                        """.format(title=search_keywords, sub_title=search_keywords, text_contents=search_keywords)

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        # print(result)
        self.commit()
        # self.close()
        return result

    def get_searchGuideline_type(self, search_types):
        sql_cmd = """SELECT *
                            FROM WorkingRightsWithID
                            WHERE type LIKE '%{type}%'
                            """.format(type=search_types)

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        # print(result)
        self.commit()
        # self.close()
        return result

    # function used to get the data in recycle_area, and display in the wastemap page
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
