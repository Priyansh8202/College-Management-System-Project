#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python

print("Content-Type:text/html")
print()

import cgi
import pymysql

aa=cgi.FieldStorage()

MemT=aa.getvalue("m")
BookI=aa.getvalue("b")
RN=aa.getvalue("r")
BkT=aa.getvalue("bt")
FiN=aa.getvalue("f")
LsN=aa.getvalue("l")
Aut=aa.getvalue("au")
DBr=aa.getvalue("db")
EM=aa.getvalue("ad")
DtD=aa.getvalue("dd")
PsC=aa.getvalue("pc")
LnD=aa.getvalue("dl")
MobN=aa.getvalue("mn")
bk=aa.getvalue("bkn")
print(MemT,BookI,RN,BkT,FiN,Aut,LsN,DBr,EM,DtD,PsC,LnD,MobN,bk)

conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("insert into library_management (membertype,bookid,rollno,booktitle,firstname,lastname,author,dateborrowed,email,duedate,postcode,loandays,mobileno,bookname) "
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(MemT,BookI,RN,BkT,FiN,LsN,Aut,DBr,EM,DtD,PsC,LnD,MobN,bk))
conn.commit()
print("data inserted")


