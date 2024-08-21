"""Bearbeitung Aufgabe 04"""

import json
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db = mysql.connector.connect(
    host="localhost", user="root", password=os.getenv("MY_KEY")
)
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


class EditColumns:
    """Class to Edit a Squad, Member or power"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def add_new_data(self, what_to_add):
        """Adds a New Squad, Member or Power"""
        if what_to_add == "squad":
            e1 = str(input("Gebe den Namen des squads ein: "))
            e2 = str(input("Gebe die Stadt des squads ein: "))
            e3 = int(input("Gründungsdatum angeben: "))
            e4 = str(input("Gebe den status des squads ein: "))
            e5 = str(input("Gebe die Geheimbasis an: "))
            e6 = int(input("Gebe an ob das squad acitv ist oder nicht: "))
            squad_sql = f"""INSERT INTO squads
            (squadName, homeTown, formed, status, secretBase, active)
            VALUES ("{e1}", "{e2}", "{e3}", "{e4}", "{e5}", "{e6}");"""
            self.cursor.execute(squad_sql)
            self.connection.commit()
            print("\nDein Squad wurde hinzugefügt\n")
        if what_to_add == "member":
            e1 = str(input("Gebe den Namen des Members ein: "))
            e2 = int(input("Gebe das Alter des Mebers ein: "))
            e3 = str(input("Gebe die geheime Identität des Members ein: "))
            e4 = int(input("zu welchem Team gehört der Member: "))
            member_sql = f"""INSERT INTO members (name, age, secretIdentity)
            VALUES ("{e1}", "{e2}", "{e3}");"""
            self.cursor.execute(member_sql)
            self.connection.commit()
            print("\nDer Member wurde hinzugefügt\n")

    def del_data(self, what_to_del):
        """Deletes a chosen Squad, Member or power"""
        if what_to_del == "squad":
            squad_del_id = input("gebe die ID des zu löschenden squads ein: ")
            squad_members_sql = f"""DELETE FROM squadMembers
            WHERE squadID = {squad_del_id} """
            self.cursor.execute(squad_members_sql)
            self.connection.commit()
            squad_sql = f"""DELETE FROM squads WHERE squadID = {squad_del_id} """
            self.cursor.execute(squad_sql)
            self.connection.commit()
            print("\nDas Squad wurde gelöscht\n")

        if what_to_del == "member":
            member_del_id = input("gebe die ID des zu löschenden members an: ")
            squad_members_sql = f"""DELETE FROM squadMembers
            WHERE memberID = {member_del_id} """
            self.cursor.execute(squad_members_sql)
            self.connection.commit()
            member_powers_sql = (
                f"""DELETE FROM memberPowers WHERE memberID = {member_del_id}"""
            )
            self.cursor.execute(member_powers_sql)
            self.connection.commit()
            member_sql = f"""DELETE FROM members WHERE memberID = {member_del_id} """
            self.cursor.execute(member_sql)
            self.connection.commit()
            print("\nDer Member wurde gelöscht\n")

    def edit_data(self, what_to_edit):
        """edit a chosen squad, member or power"""
        if what_to_edit == "squad":
            squad_id = int(
                input("gebe die Id des squads ein, dass du bearbeiten möchtest ")
            )
            e1 = int(input("""was möchtest du ändern? (1-6)"""))
            if e1 == 1:
                new_squadname = str(input("gebe den neuen squadname ein: "))
                squad_name_edit = f"""UPDATE squads SET squadName = "{new_squadname}" 
                WHERE squadID = "{squad_id}" """
                self.cursor.execute(squad_name_edit)
                self.connection.commit()
                print("\nSquadname wurde geändert\n")


with open(
    "/home/yw/einarbeitung/03_Dateiformate/base1.json", "r", encoding="utf-8"
) as file:
    datei = json.load(file)
database = Database(db)
database.create_database()
database.create_tables()
database.insert_data(datei)
editcolumns = EditColumns(db)
editcolumns.edit_data("squad")
editcolumns.del_data("member")
