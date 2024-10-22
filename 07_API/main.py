"""Bearbeitung Aufgabe 07"""

from typing import List, Dict
import os
from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user=os.getenv("USER"),
    password=os.getenv("MY_KEY")
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS superhero_db")
db = mysql.connector.connect(
    host="localhost",
    user=os.getenv("USER"),
    password=os.getenv("MY_KEY"),
    database="superhero_db"
)

@app.get("/only-squads/", response_model=List[dict])
def all_squads():
    """Ausgabe aller squads"""
    cursor_squads = db.cursor(dictionary=True)
    query = "SELECT * FROM squads;"
    cursor_squads.execute(query)
    results = cursor_squads.fetchall()
    return results

@app.get("/only-members/", response_model=List[dict])
def all_members():
    """Ausgabe aller member"""
    cursor_squads = db.cursor(dictionary=True)
    query = "SELECT * FROM members;"
    cursor_squads.execute(query)
    results = cursor_squads.fetchall()
    return results

@app.get("/squads/", response_model=List[dict])
def squads_with_members():
    """Ausgabe aller Squads und deren Mitglieder"""
    cursor_squad = db.cursor(dictionary=True)
    query = """
        SELECT
            s.squadID,
            s.squadName,
            s.homeTown,
            s.formed,
            s.status,
            s.secretBase,
            s.active,
            m.memberID,
            m.name AS member_name,
            m.age,
            m.secretIdentity
        FROM
            squads s
        LEFT JOIN
            squadMembers sm ON s.squadID = sm.squadID
        LEFT JOIN
            members m ON sm.memberID = m.memberID;
    """
    cursor_squad.execute(query)
    results = cursor_squad.fetchall()

    squads_dict = {}
    for row in results:
        squad_id = row["squadID"]

        if squad_id not in squads_dict:
            squads_dict[squad_id] = {
                "squadID": row["squadID"],
                "squadName": row["squadName"],
                "homeTown": row["homeTown"],
                "formed": row["formed"],
                "status": row["status"],
                "secretBase": row["secretBase"],
                "active": row["active"],
                "members": []
            }

        if row["memberID"]:
            squads_dict[squad_id]["members"].append({
                "memberID": row["memberID"],
                "name": row["member_name"],
                "age": row["age"],
                "secretIdentity": row["secretIdentity"]
            })

    return list(squads_dict.values())

@app.get("/squads/{squad_id}")
def id_squad(squad_id: int) -> Dict:
    """Ausgabe eines squads und seiner Mitglieder anhand der ID"""
    cursor_squad = db.cursor(dictionary=True)
    squad_query = """
        SELECT
            squadName, homeTown, formed, status, secretBase, active
        FROM
            squads
        WHERE
            squadID = %s;
    """
    members_query = """
        SELECT
            m.name AS member_name, m.age, m.secretIdentity
        FROM
            members m
        JOIN
            squadMembers sm ON m.memberID = sm.memberID
        WHERE
            sm.squadID = %s;
    """

    cursor_squad.execute(squad_query, (squad_id,))
    squad_info = cursor_squad.fetchone()

    if not squad_info:
        return {"error": "Squad not found"}

    cursor_squad.execute(members_query, (squad_id,))
    members = cursor_squad.fetchall()

    result = {
        "squad": squad_info,
        "members": members
    }

    return result

@app.delete("/squads/delete/{squad_id}")
def delete_squad(squad_id: int) -> Dict:
    """Löschen eines squads anhand seiner ID"""
    cursor_squad = db.cursor(dictionary=True)
    delete_query = """
        DELETE FROM squads
        WHERE squadID = %s;"""
    cursor_squad.execute(delete_query, (squad_id,))
    db.commit()

    return {"message": "Squad deleted", "rows_affected": cursor_squad.rowcount}

class SquadUpdate(BaseModel):
    squadName: str
    homeTown: str
    formed: int
    status: str
    secretBase: str
    active: bool

@app.put("/squads/edit/{squad_id}")
def update_squad(squad_id: int, squad: SquadUpdate) -> Dict:
    """Aktualisiert einen Squad anhand seiner ID"""

    cursor_squad = db.cursor(dictionary=True)
    update_query = """
        UPDATE squads
        SET squadName = %s, homeTown = %s, formed = %s, status = %s, secretBase = %s, active = %s
        WHERE squadID = %s;
    """
    cursor_squad.execute(update_query, (squad.squadName, squad.homeTown,
    squad.formed, squad.status, squad.secretBase, squad.active, squad_id))
    db.commit()

    return {"message": "Squad updated successfully", "rows_affected": cursor_squad.rowcount}

class MemberUpdate(BaseModel):
    name : str
    age : int
    secretIdentity : str

@app.put("/members/edit/{member_id}")
def update_member(member_id: int, member: MemberUpdate) -> Dict:
    """Aktualisiert einen Member anhand seiner ID"""

    cursor_member = db.cursor(dictionary=True)
    update_query = """
       UPDATE members
       SET name = %s, age = %s, secretIdentity = %s
       Where memberID = %s;
    """
    cursor_member.execute(update_query, (member.name, member.age, member.secretIdentity, member_id))
    db.commit()

    return {"message": "Member Updated successfully", "rows_affected": cursor_member.rowcount}
