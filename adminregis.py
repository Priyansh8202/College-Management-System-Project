#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python
print("Content-Type:text/html")
print()

import cgi
import pymysql

aa=cgi.FieldStorage()

f=aa.getvalue("fn")
l=aa.getvalue("ln")
gen=aa.getvalue("gender")
phone=aa.getvalue("p")
address=aa.getvalue("ad")
em=aa.getvalue("email")
pas=aa.getvalue("psw")

conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("insert into adminregisteration values(%s,%s,%s,%s,%s,%s,%s)",(f,l,gen,phone,address,em,pas))
conn.commit()
print("data inserted!")


