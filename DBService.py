from select import select
from flask import Flask,request,redirect,session
# from flask.ext.session import Session
import sqlite3 as sql
import hashlib
conn = sql.connect("./db/linun.db")
# conn.execute("CREATE DATABASE linun;")
# conn.execute("CREATE TABLE LoginService(userid varchar(255), username varchar(255), password varchar(255), PRIMARY KEY(userid))")
# conn.execute("CREATE TABLE user (userid varchar(255), name varchar(255), DateofBirth varchar(255), ParentName varchar(255) , score float, PRIMARY KEY(userid))")
class UserService:
    def __init__(self,db_name):
        self.conn = sql.connect(db_name)
        self.uid = "0"
        self.information = []
    def insertUser(self,userid, name, DOB, Parentname, score,username,password):
        self.conn.execute("INSERT INTO user VALUES ('"+ str(userid)+"','"+str(name)+"','"+str(DOB)+"','" +str(Parentname)+"','"+ str(score)+"');")
        password = hashlib.md5(password.encode()).hexdigest() #md5 encrypt
        self.conn.execute("INSERT INTO LoginService VALUES('"+str(userid)+"','"+str(username) +"','"+str(password)+"');")
        self.conn.commit()
    
    def selectUser(self):
        cur = self.conn.cursor()
        res = []
        for row in cur.execute("SELECT * from user order by userid"):
            res.append(row)
        return res

    def selectLogin(self):
        cur = self.conn.cursor()
        res = []
        for row in cur.execute("SELECT * from LoginService order by userid"):
            res.append(row)
        return res
    def getInfor(self):
        res = []
        cur = self.conn.cursor()
        for row in cur.execute("SELECT * from user where userid = '"+str(self.uid)+"'"):
            # print("row:",row)
            res.append(row)
        return res
    def LoginTask(self,username,password):
        accounts = self.selectLogin()
        for account in accounts:
            if (username == account[1] and password == account[2]):
                self.uid = account[0]
                return 1
        return 0
    def closeDatabase(self):
        self.conn.close()
    def printID(self):
        print(self.uid)
    def update(self,score,uid):
        print("UPDATE user SET score = "+str(score)+" WHERE userid = '"+str(uid)+"' ;")
        self.conn.execute("UPDATE user SET score = "+str(float(score))+" WHERE userid = '"+str(uid)+"' ;")
        self.conn.commit()

# us = UserService("./db/linun.db")
# print(us.LoginTask("admin","21232f297a57a5a743894a0e4a801fc3")) 
# print(us.getInfor())
# us.printID()
# insertUser("003","admin1","29/07","abc",1,"admin","admin",conn)
# print(selectLogin(conn))


