#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python
print("Content-Type:text/html")
print()

import cgi
import pymysql


print('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Marksheet</title><style type="text/css">')
print('body{background-color: white;font-family: Calibri; color:white;}.container{padding: 20px;  white; background-image: url(https://images.pexels.com/photos/1764702/pexels-photo-1764702.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);background-repeat: no-repeat;background-size: 100% 100%}')
print('div{ padding: 10px 0;}.textbox{height: 22px;width: 50px;}.butt{height: 25px;width: 100px;}th {font-size: 23px;}</style></head>')
print('<body><div class="container"><h1 style="text-align:center; font-size:60px; color:white;"><b>STUDENT MARKSHEET</b></h1>')
print('<div style="background-image: url(https://www.bosphorusdesign.com/wp-content/uploads/2022/02/bosphorusdesign-com-1.jpeg); background-repeat: no-repeat; background-size:100% 100%; padding-top: 100px; padding-left: 100px; padding-bottom: 50px;"><h1 style="font-size: 50px; color: white; margin-left:-60px; margin-top: -90px;">Student Details</h1><form action="mark1.py" method="get">')


print('<table border="0" height="60" width="1000px" style="font-size:25px;">')
print('<tr><th align="left">Enter Name</th><td align="left"><input type="text" name="na"></td><th align="right">Roll No.</th><td align="right"><input type="number" name="rn"></td></tr>')
print('<tr><th align="left">Father Name</th><td align="left"><input type="text" name="fn"></td><th align="right">Mother Name</th><td align="right"><input type="text" name="mn"></td></tr>')
print('<tr><th align="left">Date Of Birth</th><td align="left"><input type="date" name="db"></td><th align="right">Email Id</th><td align="right"><input type="email" name="em"></td></tr>')
print('<tr><th align="left">School Name</th><td align="left"><input type="text" name="sn"></td><th align="right">Contact No.</th><td align="right"><input type="number" name="cn"></td></tr>')
print('<tr><th align="left">Enter gender</th><td align="left"><input type="radio" name="gen" value="female">Female<input type="radio" name="gen" value="male">male</td></tr>')
print('<tr><td><input type="reset" name="res1" value="RESET" style="width:120px; height: 40px; font-size:20px; margin-top:20px; margin-left: 25px;"></td><td><a href="Homepage.html"><input type="button" value="Exit" style="width:120px; height: 40px; font-size:20px; margin-top:20px; margin-left:20px;"></a></td></tr></table>')

print('<br><br><h1 style="font-size: 40px; color: white;  margin-top: 0px; background-color:darkgray; margin-left: -100px; padding:10px;">Grades Point Obtained</h1>')
		

print('<table border="0" height="200" width="1200"><tr style="font-size: 27px;"><b><th>SUBJECT</th><th>MARKS OBTAINED</th><th>PASSING MARKS</th><th>TOTAL MARKS</th></b></tr>')
print('<tr><th>MultiMedia Concept & Application</th><td style="text-align:center;"><input type="number" name="math" class="textbox"></td><td style="text-align:center; font-size: 35px;">33</td><td style="text-align:center;"><label style="font-size: 25px; background-color:white; color:black;">100</label></td></tr>')
print('<tr><th>Artificial Intelligence</th><td style="text-align:center;"><input type="number" name="che" class="textbox"></td><td style="text-align:center; font-size: 35px;">33</td><td style="text-align:center;"><label style="font-size: 25px; background-color:white; color:black;">100</label></td></tr>')
print('<tr><th>Web Technology</th><td style="text-align:center;"><input type="number" name="phy" class="textbox"></td><td style="text-align:center; font-size: 35px;">33</td><td style="text-align:center;"><label style="font-size: 25px; background-color:white; color:black;">100</label></td></tr>')
print('<tr><th>Introduction To .NET</th><td style="text-align:center;"><input type="number" name="pro" class="textbox"></td><td style="text-align:center; font-size: 35px;">33</td><td style="text-align:center;"><label style="font-size: 25px; background-color:white; color:black;">100</label></td><td style="text-align:center"><input type="reset" name="res2" value="RESET" class="butt"></td></tr>')
print('<tr><th>Web Technology (Lab)</th><td style="text-align:center;"><input type="number" name="eng" class="textbox"></td><td style="text-align:center; font-size: 35px;">33</td><td style="text-align:center;"><label style="font-size: 25px; background-color:white; color:black;">100</label></td></tr>')
print('<tr><th>GRAND TOTAL</th><td style="text-align:center;"><input type="number" name="gt" class="textbox"></td><td style="text-align:center;"><label style="font-size: 30px; background-color:white; color:black;">165</label></td><td style="text-align:center;"><label style="font-size: 30px; background-color:white; color:black;">500</label></td></tr>')
print('<tr><th>CGPA</th><td style="text-align:center;"><input type="number" name="cg" class="textbox"></td></tr>')
print('<tr><th>RESULT</th><td style="text-align:center;"><input type="text" name="res" class="butt"></td><th>GRADE</th><td><input type="text" name="gra" class="butt"></td><td style="text-align:center"><input type="submit" name="sub2" class="butt" value="SUBMIT"></td></tr>')
print('</table></form></div></div></body></html>')

