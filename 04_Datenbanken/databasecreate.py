"""Bearbeitung Aufgabe 04"""

import json
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="superhero_db"
)


class Database:
    """erstellung der Datenbank und Tables"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_database(self):
        """erstellung Datenbank"""
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
        self.connection.commit()

    def create_tables(self):
        """erstellung der Tables"""
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
            secretIdentity VARCHAR(50)
        );
        """
        self.cursor.execute(create_members_table)
        create_squadmembers_table = """
        CREATE TABLE IF NOT EXISTS squadMembers (
            squadID INT,
            memberID INT,
            PRIMARY KEY (squadID, memberID),
            FOREIGN KEY (squadID) REFERENCES squads(squadID),
            FOREIGN KEY (memberID) REFERENCES members(memberID)
        );
        """
        self.cursor.execute(create_squadmembers_table)
        create_powers_table = """
            CREATE TABLE IF NOT EXISTS powers (
            powerID INT AUTO_INCREMENT PRIMARY KEY,
            powers VARCHAR(255)
            );
            """
        self.cursor.execute(create_powers_table)
        create_memberpowers_table = """
            CREATE TABLE IF NOT EXISTS memberPowers(
            powerID INT,
            memberID INT,
            PRIMARY KEY(powerID, memberID),
            FOREIGN KEY (powerID) REFERENCES powers(powerID),
            FOREIGN KEY (memberID) REFERENCES members(memberID))"""
        self.cursor.execute(create_memberpowers_table)
        self.connection.commit()

    def insert_data(self, data):
        """Daten in Tables einfügen und verknüpfen"""
        with open(
            "/home/yw/einarbeitung/03_Dateiformate/base1.json", "r", encoding="utf-8"
        ) as json_file:
            data = json.load(json_file)

        for squad in data:
            squad_sql = """
            INSERT INTO squads (squadName, homeTown, formed, status, secretBase, active)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            squad_values = (
                squad["squadName"],
                squad["homeTown"],
                squad["formed"],
                squad["status"],
                squad["secretBase"],
                squad["active"],
            )
            self.cursor.execute(squad_sql, squad_values)
            squad_id = self.cursor.lastrowid
            for member in squad["members"]:
                member_sql = """
                INSERT INTO members (name, age, secretIdentity)
                VALUES (%s, %s, %s)
                """
                member_values = (
                    member["name"],
                    member["age"],
                    member["secretIdentity"],
                )
                self.cursor.execute(member_sql, member_values)
                member_id = self.cursor.lastrowid
                self.cursor.execute(
                    """
                    INSERT INTO squadMembers (squadID, memberID)
                    VALUES (%s, %s)
                    """,
                    (squad_id, member_id),
                )

                for power in member["powers"]:
                    power_sql = """
                    INSERT INTO powers (powers)
                    VALUES (%s)
                    """
                    power_value = (power,)
                    self.cursor.execute(power_sql, power_value)
                    power_id = self.cursor.lastrowid
                    self.cursor.execute(
                        """
                        INSERT INTO memberPowers (powerID, memberID)
                        VALUES (%s, %s)
                        """,
                        (power_id, member_id),
                    )

        self.connection.commit()


with open(
    "/home/yw/einarbeitung/03_Dateiformate/base1.json", "r", encoding="utf-8"
) as file:
    datei = json.load(file)
database = Database(db)
database.create_database()
database.create_tables()
database.insert_data(datei)
