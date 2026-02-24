import pymysql

class DbUtils:
    def connect(self):
        return pymysql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="pydb",
        )