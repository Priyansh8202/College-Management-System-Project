#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python
print("Content-Type:text/html")
print()

import cgi
import pymysql

print('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">')
print('<title>Student Marksheet Search!!</title><style type="text/css">')

print('body{background-image:url(https://images.pexels.com/photos/1764702/pexels-photo-1764702.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);background-repeat:no-repeat;')
print('background-size:cover; font-family: Calibri; color:white;}input {border: none;}')
print('.butt{height: 30px;width: 120px;</style></head>')
print('<body><center><button style="background-color: black; color: lightblue; height: 100px; width: 550px; font-size: 50px; font-family: calibri; border-color: white; border-width: 4px;">STUDENT DATA SERACH</button></center><br>')
print('<hr style="background-color: white; height: 3px; border: none;">')

print('<div style=" border-color: black; width:1350px; height: 200px; background-color:black; background-repeat: no-repeat; background-size: cover;">')
print('<form action="" method="get">')
print('<Center><table style="font-size:30px; margin-top:50px; "><tr><th align="right" style="color:lightgray;">ENTER STUDENT Roll NO :</th>')
print('<td align="right"><input type="text" name="rc" style="height:30px; width:200px;"></td></tr><br>')
print('<tr><center><th><input type="submit" name="di" class="butt" value="SEARCH"></th><td align="left"><a href="Homepage.html"><input type="button" name="ex" class="butt" value="EXIT"></input></a></td></tr>')
print('</table></center></form></div></center><br><center>')
print('</div')




print('<div style=" border-color: black; width:1200px; height: 100px; background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT96UXWNYMMonDDFSXaNVO7ha-vOQb1It5aw&usqp=CAU); background-repeat: no-repeat; background-size: cover;">')
print("<table border='1'>")
print("<tr><th>Name</th><th>Father Name</th><th>Mother Name</th><th>College Name</th>")
print("<th>Gender</th><th>DOB</th><th>Roll No.</th><th>Mobile No</th><th>Email Id</th><th>MC&A</th><th>AI</th><th>.Net</th><th>Webtech</th><th>WebTech Lab</th><th>Grand Total</th><th>CGPA</th><th>Resut</th><th>Grade</th></tr>")

ff = cgi.FieldStorage()

rn=ff.getvalue("rc")
conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur = conn.cursor()
cur.execute("select * from markdetails where roll_no = %s", (rn))
data = cur.fetchall()

for i in data:
    print("<tr><td>",i[0],"</td>")
    print("<td>",i[1],"</td>")
    print("<td>",i[2],"</td>")
    print("<td>",i[3],"</td>")
    print("<td>",i[4],"</td>")
    print("<td>",i[5],"</td>")
    print("<td>",i[6],"</td>")
    print("<td>",i[7],"</td>")
    print("<td>",i[8],"</td>")
    print("<td>",i[9],"</td>")
    print("<td>",i[10],"</td>")
    print("<td>",i[11],"</td>")
    print("<td>",i[12],"</td>")
    print("<td>",i[13],"</td>")
    print("<td>",i[14],"</td>")
    print("<td>",i[15],"</td>")
    print("<td>",i[16],"</td>")
    print("<td>",i[17],"</td></tr>")

conn.commit()
print('</tr></table></div></center></body></html>')
