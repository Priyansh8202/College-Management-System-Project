#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python

print("Content-Type:text/html")
print()

import cgi
import pymysql

print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Upadte Student Details</title>')
print('<style>')
print('.box')
print('{height:20px; width: 500px; background-color: lightgray; border-radius: 200px; font-size: 15px;  color: red;}')
print('th{ font-size: 20px;}')
print('td{ margin-left;50px;}')
print('</style>')
print('</head>')
print('<body style="background-color:powderblue;">')
print('<center><h1 style="font-size:35px; margin-top:0px; font-family:forte;">Update Student Details Form</h1></center>')
print('<hr style="height:2px;border-width:0;color:black;background-color:black;text-align:left;margin-left:5">')
print('<div style="background-image: url(https://media.istockphoto.com/photos/text-with-notepad-keyboard-decorative-vase-and-fountain-pen-on-wooden-picture-id1217531052?k=20&m=1217531052&s=612x612&w=0&h=7AGZwe63ElW-upa2lonUTGKQTx6AVCL_MWZ0vyJwI7Y=); height:810px; width:700px; float:left; background-size: 100% 100%;">')
print('</div>')
print('<div style="background-image:url(https://images.unsplash.com/photo-1500989145603-8e7ef71d639e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=876&q=80); background-color:white; height:810px; width:600px; float:right; background-size:cover;">')
print('<form action="" method="get" >')
print('<table style="height:260px; width: 650px;" >')

aa=cgi.FieldStorage()

roln=aa.getvalue("stu")

conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("select * from sturegister where rollno=%s",(roln))
data=cur.fetchall()
for i in data:
    print('<tr><th><label>Student Roll No:<span style="color:red; font-family:forte;">*</span></label></th></tr><br>')
    print('<tr><th><input type="text" placeholder="Enter Student Roll No" name="stu" autocomplete="off" required class="box" value={0}></th></tr>'.format(i[0]))
    print('<tr><th><label>Student Name:<span style="color:red; font-family:forte;">*</span></label></th></tr>')
    print('<tr><th><input type="text" placeholder="Enter ur Name" name="n" autocomplete="off" class="box" value={0}></th></tr>'.format(i[1]))
    print('<tr> <th><label>Father Name:</label></th> </tr>')
    print('<tr><th><input type="text" name="fn" placeholder="Father Name" autocomplete="off" class="box" value={0}></th></tr>'.format(i[2]))
    print('<tr> <th><label>Mother Name:</label></th> </tr>')
    print('<tr> <th><input type="text" name="m" placeholder="Mother Name" autocomplete="off" class="box" value={0}></th></tr>' .format(i[3]))
    print('<tr><th><label>Date Of Birth:</label></th></tr>')
    print('<tr><th><input type="date" name="db" placeholder="DOB" autocomplete="off" class="box" value={0}></th></tr>' .format(i[4]))
    print('<tr> <th><label>Address:</label></th> </tr>')
    print('<tr> <th><input type="text" name="ad" placeholder="Enter ur Address" autocomplete="off"  class="box" value={0}></th></tr>' .format(i[5]))
    print('<tr><th><label>City:</label></th></tr>')
    print('<tr><th><input type="text" name="cy" placeholder="Enter ur City" autocomplete="off" class="box" value={0}></th></tr>'  .format(i[6]))
    print('<tr> <th><label>Mobile:</label></th></tr>')
    print('<tr><th><input type="text" name="mn" placeholder="Enter ur Mobile No" autocomplete="off" class="box" value={0}></th></tr>'  .format(i[7]))
    print('<tr><th><label>E-Mail:</label></th> </tr>')
    print('<tr> <th><input type="text" name="em" placeholder="Enter ur Email" autocomplete="off" class="box" value={0}></th> </tr>'  .format(i[8]))
    print('<tr> <th><label>Course:</label></th></tr>' )
    print('<tr><th><label><input list="course" placeholder="Select Any UG Course" name="cu" autocomplete="off" class="box" value={0}></label>'.format(i[9]))
    print('<datalist id="course">')
    print('<option value="BCA"></option>')
    print('<option value="BCA-CLOUD"></option>')
    print('</datalist>')
    print('</h3></th></tr>')
    print('<tr><th><label>Department:</label></th></tr>')
    print('<tr><th><label><input list="depart" placeholder="Select Any Department" name="dp" autocomplete="off" class="box" value={0}></label>'.format(i[10]))
    print('<datalist id="depart"><option value="Computer Applications"><option value="Civil Engineering"><option value="Mechanical Engineering"><option value="Electrical Engineering"><option value="Artificial Engineering">')
    print('<option value="Cloud Computing"><option value="Computer Science and Engineering"></datalist></h3></th></tr>')
    print('<tr><th><label>Gender:</label></th></tr>')
    print('<tr><th><label><input list="gen" placeholder="Select Gender" name="gen" autocomplete="off" class="box" value={0}></label>'.format(i[11]))
    print('<datalist id="gen"><option value="Male"><option value="female"></datalist></h3></th></tr></form></table>')


aa=cgi.FieldStorage()
roln=aa.getvalue("stu")
na=aa.getvalue('n')
fa=aa.getvalue('fn')
mn=aa.getvalue('m')
d=aa.getvalue('db')
add=aa.getvalue('ad')
ct=aa.getvalue('cy')
mo=aa.getvalue('mn')
mail=aa.getvalue('em')
c=aa.getvalue('cu')
dept=aa.getvalue('dp')
gend=aa.getvalue('gen')
conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("update sturegister set studentName=%s,fatherName=%s,motherName=%s,DOB=%s,address=%s,city=%s,mobile=%s,email=%s,course=%s,department=%s,gender=%s where rollno=%s",(na,fa,mn,d,add,ct,mo,mail,c,dept,gend,roln))
conn.commit()

print('<input type="submit" value="Update"  style="margin-left: 75px; margin-top:20px; height:30px; width:500px; background-color:darkblue; color:white; font-size:20px;">')
print('<a href="studentprofile.html"><input type="button" value="Back"  style="margin-left: 75px; margin-top:20px; height:30px; width:500px; background-color:darkblue; color:white; font-size:20px;"></a>')
print('</table></form></body></html>')
print("<html><body><script>alert('data inserted');</script></body></html>")
