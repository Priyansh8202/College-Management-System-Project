#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python
print("Content-Type:text/html")
print()

import cgi
import pymysql

ff=cgi.FieldStorage()
name=ff.getvalue("na")
rollno=ff.getvalue("rn")
fname=ff.getvalue("fn")
mname=ff.getvalue("mn")
dob=ff.getvalue("db")
email=ff.getvalue("em")
sname=ff.getvalue("sn")
contact=ff.getvalue("cn")
gender=ff.getvalue("gen")
math=ff.getvalue("math")
che=ff.getvalue("che")
phy=ff.getvalue("phy")
pro=ff.getvalue("pro")
eng=ff.getvalue("eng")
gt=ff.getvalue("gt")
cgpa=ff.getvalue("cg")
result=ff.getvalue("res")
gra=ff.getvalue("gra")



#!print(name,fname,mname,sname,gender,dob,rollno,contact,email,math,che,phy,pro,eng,gt,cg,res,gra)

conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("insert into markdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,fname,mname,sname,gender,dob,rollno,contact,email,math,che,phy,pro,eng,gt,cgpa,result,gra))
conn.commit()
print("<html><body><script>alert('data inserted');</script></body></html>")

