import sqlite3

def getConnection():
    con = sqlite3.connect("user.db")
    return con
