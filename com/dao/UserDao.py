import sqlite3

con = sqlite3.connect("User.db")


def createTable():
    con.execute("create table if not exists std(uid INTEGER PRIMARY KEY AUTOINCREMENT,name text,address text,city text,course text)")
    con.commit()
    
def saveUser(name,address,ct,course):
    data = (name,address,ct,course)
    con.execute("insert into std(name,address,city,course) values(?,?,?,?)",data)
    con.commit()
    
def updateUser(uid,name,address,ct,course):
    data = (name,address,ct,course,uid)
    con.execute("update std set name=? ,address=?,city=?,course=? where uid=?",data)
    con.commit()
    
def deleteUser(uid):
    data = (uid)
    con.execute("delete from std where uid='"+uid+"'")
    con.commit()

def getalluser():
    cur = con.execute("select * from std")
    data = cur.fetchall()
    return data

def getUser(uid):
    cur = con.execute("select * from std where uid='"+uid+"'")
    data = cur.fetchall()
    return data

def search(search):
    cur = con.execute("select * from std where uid like '%"+search+"%' or name like '%"+search+"%' or address like '%"+search+"%' or city like '%"+search+"%' or course like '%"+search+"%'")
    data = cur.fetchall()
    return data
    
def clear():
    con.execute("delete from std where 1=1")
    con.commit()
 