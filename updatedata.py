#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python

print("Content-Type:text/html")
print()

import cgi
import pymysql

print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Update Student Details</title>')
print('<style>')
print('.box')
print('{height:30px; width: 500px; background-color: lightgray; border-radius: 200px; font-size: 15px;  color: red;}')
print('th{ font-size: 20px;}')
print('td{ margin-left;50px;}')
print('</style>')
print('</head>')
print('<body style="background-color:powderblue;">')
print('<center><h1 style="font-size:45px; margin-top:0px; font-family:forte;">Update Student Details Form</h1></center>')
print('<hr style="height:2px;border-width:0;color:black;background-color:black;text-align:left; margin-left:5;">')
print('<div style="background-image: url(https://image.shutterstock.com/image-photo/update-software-computer-program-upgrade-600w-1121392865.jpg); height:550px; width:700px; float:left; background-size: 100% 100%;">')
print('</div>')
print('<div style="background-image:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVdecgcI3h_nQcuOkstvi0SYxWc6FmnYCQjw&usqp=CAU); background-color:white; height:550px; width:600px; float:right; background-size: cover;">')
print('<form action="updatedetail.py" method="get" >')
print('<table style="height:260px; width: 650px;" ><br><br><br><br>')
print('<tr><th><label style="color:brown; font-family:forte; font-size:50px;">Student Roll No:<span style="color:red; font-family:forte;">*</span></label></th></tr>')
print('<tr><th><input type="text" placeholder="Enter Student Roll No" name="stu" autocomplete="off" required class="box"></th></tr>')
print('<tr><td><input type="submit" value="Search"  style="font-size:25px; margin-left: 75px; margin-top:20px; height:35px; width:500px; background-color:darkblue; color:white;"></td></tr>')
print('<tr><td><a href="studentprofile.html"><input type="button" value="Back"  style="margin-left: 75px; margin-top:20px; height:30px; width:500px; background-color:darkblue; color:white; font-size:20px;"></a></td></tr>')
print('</table></form></body></html>')


