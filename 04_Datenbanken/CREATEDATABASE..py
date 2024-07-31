"""Bearbeitung Aufgabe 04"""

import mysql.connector
import json

db = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = db.cursor()


class CreateDb:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def createDatabase(self):
        cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
        self.connection.commit()

    def createTables(self):
        create_squads_table = """
        CREATE TABLE IF NOT EXISTS squads (
            squadName VARCHAR(50),
            homeTown VARCHAR(50),
            formed INT,
            status VARCHAR(15),
            secretBase VARCHAR(50),
            active TINYINT(1)
        );
        """
        self.cursor.execute(create_squads_table)

        create_members_table = """
        CREATE TABLE IF NOT EXISTS members (
            name VARCHAR(50),
            age INT,
            secretIdentity VARCHAR(50)
            )"""

        self.cursor.execute(create_members_table)

        create_powers_table = """
            CREATE TABLE IF NOT EXISTS powers (
            power VARCHAR(50)
            )
            """
        self.cursor.execute(create_powers_table)

        self.connection.commit()


conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="superhero_db"
)


cursor = conn.cursor()
cursor.execute("USE superhero_db")

database = CreateDb(conn)
database.createTables()
conn.close()
