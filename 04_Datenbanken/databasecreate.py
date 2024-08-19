"""Bearbeitung Aufgabe 04"""

import mysql.connector
import json

db = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")


class Create_db:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_database(self):
        cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
        self.connection.commit()

    def create_tables(self):
        create_squads_table = """
        CREATE TABLE IF NOT EXISTS squads (
            squadID INT AUTO_INCREMENT PRIMARY KEY,
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
            secretIdentity VARCHAR(50),
            squadID INT,
            FOREIGN KEY (squadID) REFERENCES squads(squadID),
            powerID INT CONSTRAINT
        )
        """
        self.cursor.execute(create_members_table)

        create_powers_table = """
            CREATE TABLE IF NOT EXISTS powers (
            powerID INT AUTO_INCREMENT PRIMARY KEY,
            power VARCHAR(50)
            )
            """
        self.cursor.execute(create_powers_table)
        self.cursor.execute(
            """
            ALTER TABLE members
            ADD CONSTRAINT powerID
            FOREIGN KEY (powerID) REFERENCES members(powerID);
            """
        )

        self.connection.commit()

    def insert_data(self):
        with open("base1.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

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
            squadID = self.cursor.lastrowid

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
            memberID = self.cursor.lastrowid

        for power in member["powers"]:
            powerSql = """
                INSERT INTO powers (power, IDmember)
                VALUES (%s, %s)
                    """
            powerValues = (power, memberID)
            self.cursor.execute(powerSql, powerValues)

        self.connection.commit()

    class removeColumn:
        pass


conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="superhero_db"
)

db = Create_db(conn)
db.create_tables()
db.insert_data()
conn.close()
