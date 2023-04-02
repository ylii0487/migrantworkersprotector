import datetime
import mysql.connector
import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder


class MySQLDatabase():

    def open_ssh_tunnel(verbose=False):
        """Open an SSH tunnel and connect using a username and password.

        :param verbose: Set to True to show logging
        :return tunnel: Global SSH tunnel connection
        """

        sshtunnel.SSH_TIMEOUT = 30.0
        sshtunnel.TUNNEL_TIMEOUT = 30.0

        ssh_host = '20.5.240.150'
        ssh_username = 'azureuser'
        ssh_password = 'fit5120'
        ssh_pkey_file = "C:/Users/liyon/Desktop/2023S1/FIT5120/migrantworkersprotector-main/migrantworkersprotector/fit5120tp09au_key.pem"

        if verbose:
            sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

        global tunnel
        tunnel = SSHTunnelForwarder(
            (ssh_host, 22),
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            ssh_pkey=ssh_pkey_file,
            remote_bind_address=('10.1.0.4', 3306)
        )

        tunnel.start()

    def __init__(self):

        """Connect to a MySQL server using the SSH tunnel connection

            :return connection: Global MySQL database connection
            """

        database_host = '10.1.0.4'
        database_username = 'developer'
        database_name = 'worker'
        database_password = 'fit5120'

        self.open_ssh_tunnel()
        try:
            self.conn = pymysql.connect(host=database_host,
                                        user=database_username,
                                        passwd=database_password,
                                        port=tunnel.local_bind_port,
                                        db=database_name
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
                    age INT,
                    gender varchar(100),
                    major varchar(100) NOT NULL,
                    skills varchar(100) NOT NULL,
                    industy varchar(100),
                    experience varchar(500) NOT NULL
                    )"""

        self.cursor.execute(sql_cmd1)
        self.commit()

        # self.add_event('Happy Recycling Day', '2023-03-21 15:00:00', 'Melbourne center', 'ylii0487@student.monash.edu', 'Learn learn learn!!')

    # def add_event(self, event_topic, event_time, event_place, contact_details, event_content):
    #
    #     sql_cmd = """INSERT INTO Events(event_topic, event_time, event_place, contact_details, event_content)
    #                     VALUES('{event_topic}', '{event_time}','{event_place}', '{contact_details}', '{event_content}')
    #                     """.format(event_topic=event_topic, event_time=event_time, event_place=event_place,
    #                                contact_details=contact_details, event_content=event_content)
    #     self.cursor.execute(sql_cmd)
    #
    #     self.commit()
    #
    #     return True
    #
    # def get_allEvents(self):
    #     sql_cmd = """SELECT *
    #             FROM Events
    #             ORDER BY event_time DESC
    #             """
    #
    #     self.cursor.execute(sql_cmd)
    #
    #     result = list(self.cursor.fetchall())
    #     # print(result)
    #     self.commit()
    #
    #     return result
    #
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
