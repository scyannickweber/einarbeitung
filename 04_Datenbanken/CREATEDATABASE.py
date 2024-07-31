"""Bearbeitung Aufgabe 04"""

import mysql.connector
import json

db = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")


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
            memberID INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            secretIdentity VARCHAR(50)
            )"""

        self.cursor.execute(create_members_table)

        create_powers_table = """
            CREATE TABLE IF NOT EXISTS powers (
            powerID INT AUTO_INCREMENT PRIMARY KEY,
            powers VARCHAR(255)
            )
            """
        self.cursor.execute(create_powers_table)

        self.connection.commit()

    def insertData(self):
        with open("/home/yw/einarbeitung/03_Dateiformate/base1.json", "r") as file:
            data = json.load(file)

        for squad in data:
            squadSql = """
            INSERT INTO squads (squadName, homeTown, formed, status, secretBase, active)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            squadValues = (
                squad["squadName"],
                squad["homeTown"],
                squad["formed"],
                squad["status"],
                squad["secretBase"],
                squad["active"],
            )

            self.cursor.execute(squadSql, squadValues)

        for squad in data:
            for member in squad["members"]:
                memberSQL = """
                INSERT INTO members (name, age, secretIdentity)
                VALUES (%s, %s, %s)
                """

                memberValues = (
                    member["name"],
                    member["age"],
                    member["secretIdentity"],
                )

                self.cursor.execute(memberSQL, memberValues)

        for squad in data:
            for member in squad["members"]:
                for power in member["powers"]:
                    powerSQL = """
                        INSERT INTO powers (powers)
                        VALUES (%s)
                        """

                    powerValue = (power,)

                    self.cursor.execute(powerSQL, powerValue)
        self.connection.commit()


conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="superhero_db"
)
cursor = conn.cursor()
cursor.execute("USE superhero_db")

database = CreateDb(conn)
database.createTables()
database.insertData()
conn.close()
