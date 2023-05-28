#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python

print("Content-Type:text/html")
print()

import cgi
import pymysql

aa=cgi.FieldStorage()

emai=aa.getvalue("userid")
pas=aa.getvalue("pas")
conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("select * from adminregisteration where email=%s and pas=%s",(emai,pas))
data=cur.fetchall()
d=int(cur.rowcount)
if(d<=0):
    print("<html><body><script>alert('Please go back and enter a valid login');</script></body></html>")
else:
    print('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Home Page!!!!</title>')
    print('<style>body{background-repeat: no-repeat;background-size: cover;}</style></head>')
    print('<body style="background-image: url(https://images.unsplash.com/photo-1497633762265-9d179a990aa6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZWR1Y2F0aW9ufGVufDB8fDB8fA%3D%3D&w=1000&q=80)"><img src="ssgi.png" alt="colgpic" style="width:200px; height:160px; margin-left:800px; "><h1 style="font-family:forte; color:red; background-color:lightgray; font-size:40px; margin-left:600px; ">college Management System </h1>')
    print('<table border="0" height="250px" width="750px" style="margin-left: 600px;" >')
    print('<tr><th><a href="studentprofile.html"><button type="button" style="color:darkblue;" > <img src="https://img.icons8.com/stickers/452/student-registration.png" height ="80" width="100" ><b>Student Profile</b></button></a></th><td><a href="fee1.py"><button type="button" style=" color:darkblue;" > <img src="https://cdn-icons-png.flaticon.com/512/2496/2496311.png" height ="80" width="100" ><b>Fees Data Report</b></button></a></td>')
    print('<td><a href="marksheet.py"><button type="button" style="color:darkblue;"> <img src="https://image.shutterstock.com/image-vector/marksheet-vector-colour-flat-icon-600w-1877774443.jpg" height ="80" width="100" ><b>Marksheet Report</b></button></a></td></tr><tr><th><a href="LibraryManagement.html"><button type="button" style="color:darkblue;"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDJm32d3k3RJOWGWDHj07jf9P_JKnEP4P_9A&usqp=CAU" height ="80" width="100" ><b>Library Management</b></button></a></th>')
    print('<td><a href="marksheetdatasearch.py"><button type="button" style="color:darkblue;"> <img src="https://image.shutterstock.com/image-vector/serch-logo-uses-letters-c-260nw-413937706.jpg" height ="80" width="100" ><b>Marksheet Search</b></button></a></td><td><a href="first.html"><button type="button" style="color:darkblue;"> <img src="https://image.shutterstock.com/image-vector/exit-logout-icon-260nw-755619139.jpg" height ="80" width="100" ><b>Admin Log Out</b></button></a> </td></tr>')
    print('</table></body></html>')
    print("<html><body><script>alert('LOgin Successfully');</script></body></html>")    

conn.commit()
#!print(cur.rowcount,"record(s) deleted")



