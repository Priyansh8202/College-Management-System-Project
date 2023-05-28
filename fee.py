#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python
print("Content-Type:text/html")
print()

import cgi
import pymysql

ff=cgi.FieldStorage()

rn=ff.getvalue("rn")
sn=ff.getvalue("sn")
an=ff.getvalue("an")
ta=ff.getvalue("ta")
date=ff.getvalue("date")
pa=ff.getvalue("pa")
br=ff.getvalue("br")
ba=ff.getvalue("ba")
sem=ff.getvalue("se")

#!print(rn,sn,an,ta,date,pa,br,ba,sem)

conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("insert into fee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rn,sn,an,ta,date,pa,br,ba,sem))
conn.commit()
print("<html><body><script>alert('data inserted');</script></body></html>")
