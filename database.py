import sqlite3

class SQl():
    def __init__(self,filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def read(self,tadleName):
        self.cursor.execute(f"select * from {tadleName}")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()