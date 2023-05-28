#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python

print("Content-Type:text/html")
print()

import cgi
import pymysql

aa=cgi.FieldStorage()

roln=aa.getvalue("n")
conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("delete from sturegister where rollno=%s",(roln))
conn.commit()
#!print(cur.rowcount,"record(s) deleted")
print("<html><body><script>alert('Record(s) deleted Sucessfully!!!!!!!');</script></body></html>")


