"""Bearbeitung Aufgabe 04"""

import mysql.connector
import json

db = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="superhero_db"
)


class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def createDatabase(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
        self.connection.commit()

    def createTables(self):
        createSquadsTable = """
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
        self.cursor.execute(createSquadsTable)

        createMembersTable = """
        CREATE TABLE IF NOT EXISTS members (
            memberID INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            secretIdentity VARCHAR(50)
        );
        """
        self.cursor.execute(createMembersTable)

        createSquadMembersTable = """
        CREATE TABLE IF NOT EXISTS squadMembers (
            squadID INT,
            memberID INT,
            PRIMARY KEY (squadID, memberID),
            FOREIGN KEY (squadID) REFERENCES squads(squadID),
            FOREIGN KEY (memberID) REFERENCES members(memberID)
        );
        """
        self.cursor.execute(createSquadMembersTable)

        createPowersTable = """
            CREATE TABLE IF NOT EXISTS powers (
            powerID INT AUTO_INCREMENT PRIMARY KEY,
            powers VARCHAR(255)
            );
            """
        self.cursor.execute(createPowersTable)

        createMemberPowersTable = """
            CREATE TABLE IF NOT EXISTS memberPowers(
            powerID INT,
            memberID INT,
            PRIMARY KEY(powerID, memberID),
            FOREIGN KEY (powerID) REFERENCES powers(powerID),
            FOREIGN KEY (memberID) REFERENCES members(memberID))"""

        self.cursor.execute(createMemberPowersTable)

        self.connection.commit()

    def insertData(self, data):
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

                linkSquadMember = """
                INSERT INTO squadMembers (squadID, memberID)
                VALUES (%s, %s)
                """
                self.cursor.execute(linkSquadMember, (squadID, memberID))

                for power in member["powers"]:
                    powerSQL = """
                    INSERT INTO powers (powers)
                    VALUES (%s)
                    """
                    powerValue = (power,)
                    self.cursor.execute(powerSQL, powerValue)
                    powerID = self.cursor.lastrowid

                    linkMemberPowers = """
                    INSERT INTO memberPowers (powerID, memberID)
                    VALUES (%s, %s)
                    """
                    self.cursor.execute(linkMemberPowers, (powerID, memberID))

        self.connection.commit()


class editColumns:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def AddNewData(self, whatToAdd):
        if whatToAdd == "squad" or "Squad":
            Eingabe1 = str(input("gebe den Namen des squads ein: "))
            Eingabe2 = str(input("gebe die Stadt des squads ein: "))
            Eingabe3 = int(input("Gründungsdatum angeben: "))
            Eingabe4 = str(input("gebe den status des squads ein: "))
            Eingabe5 = str(input("gebe die Geheimbasis an: "))
            Eingabe6 = int(input("gebe an ob das squad acitv ist oder nicht: "))

            squadSQL = f"""INSERT INTO squads (squadName, homeTown, formed, status, secretBase, active)
            VALUES ("{Eingabe1}", "{Eingabe2}", "{Eingabe3}", "{Eingabe4}", "{Eingabe5}", "{Eingabe6}");"""  # funktioniert, jetzt noch für power und members

            self.cursor.execute(squadSQL)
            self.connection.commit()
        else:
            return

    def delData(self, whatToDel):
        if whatToDel == "squad" or "Squad":
            Eingabe1 = input("gebe die ID des zu löschenden squads ein: ")
            squadSQL = f"""DELETE FROM squadMembers
            WHERE squadID = {Eingabe1} """
            self.cursor.execute(squadSQL)
            self.connection.commit()

            squadSQL = f"""DELETE FROM squads 
            WHERE squadID = {Eingabe1} """
            self.cursor.execute(squadSQL)
            self.connection.commit()


with open("/home/yw/einarbeitung/03_Dateiformate/base1.json", "r") as file:
    data = json.load(file)


database = Database(db)
database.createDatabase()
database.createTables()
database.insertData(data)
editcolumns = editColumns(db)
# editcolumns.AddNewData("squad")
editcolumns.delData("squad")
