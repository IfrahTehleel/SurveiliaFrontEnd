import sqlite3


def createTable():
    connection = sqlite3.connect("login.db")
    connection.execute(
        "CREATE TABLE USERS ( USER_ID INTEGER PRIMARY KEY, USERNAME TEXT NOT NULL, PASSWORD NOT NULL, CONTACT_INFO TEXT NOT NULL UNIQUE, ADDRESS TEXT ")

    connection.execute("")
