from mimetypes import init


class User:
    def __init__(this):
        this.id = None
        this.name = None
        this.email = None
        this.phno = None
        this.gender = None
    def getId(this):
        return this.id
    def getName(this):
        return this.name
    def getEmail(this):
        return this.email
    def getphno(this):
        return this.phno
    def getGender(this):
        return this.gender
    
    def setId(this,id):
        this.id = id
    def setName(this,name):
        this.name = name
    def setEmail(this,email):
        this.email = email
    def setphno(this,phno):
        this.phno = phno
    def setgender(this,gender):
        this.gender = gender
    