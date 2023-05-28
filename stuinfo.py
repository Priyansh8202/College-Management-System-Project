#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python

print("Content-Type:text/html")
print()

import cgi
import pymysql

aa=cgi.FieldStorage()

rn=aa.getvalue("stu")
name=aa.getvalue("n")
father=aa.getvalue("fn")
mother=aa.getvalue("m")
dob=aa.getvalue("db")
address=aa.getvalue("ad")
city=aa.getvalue("cy")
mobile=aa.getvalue("mn")
email=aa.getvalue("em")
course=aa.getvalue("cu")
department=aa.getvalue("dp")
genn=aa.getvalue("gen")



#!print(rn,name,father,mother,dob,address,city,mobile,email,course,department,genn)

conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("insert into sturegister (rollno,studentName,fatherName,motherName,DOB,address,city,mobile,email,course,department,gender)"
            " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rn,name,father,mother,dob,address,city,mobile,email,course,department,genn))
conn.commit()
print("data inserted")


