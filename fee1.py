#!C:\Users\PRIYANSH GOEL\AppData\Local\Programs\Python\Python310\python
print("Content-Type:text/html")
print()

import cgi
import pymysql


print('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">')
print('<title>Fees Report</title><style type="text/css">')
print('body{background-image:url(https://ijnet.org/sites/default/files/styles/full_width_node/public/migrated/2016/07/233798733_33f14e3441_b.jpg?itok=OyFoZpSG);background-repeat:no-repeat;')
print('background-size:100% 100%;font-family: Calibri; color:white;}input {border: none;}')
print('.butt{height: 30px;width: 120px;</style></head>')
print('<body><center><button style="background-color: black; color: lightblue; height: 100px; width: 450px; font-size: 60px; font-family: calibri; border-color: white; border-width: 4px;">FEE  REPORT</button></center><br>')
print('<hr style="background-color: white; height: 3px; border: none;">')
print('<center><button style="border-color: black; width:1345px; height: 400px; background-image: url(https://images.alphacoders.com/741/74183.jpg); border: none; background-repeat:no-repeat; background-size: 1500px 400px;">')
print('<div style="background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT96UXWNYMMonDDFSXaNVO7ha-vOQb1It5aw&usqp=CAU); background-repeat: no-repeat; width:830px; height:300px; background-size:830px 300px;">')
print('<h3 style="font-size: 35px; color: white; padding-left: 0px; padding-top: 10px; font-family: cursive;"> INFORMATION</h3>')



print('<form action="fee.py" method=""><table style="font-size: 20px; width:750px; height: 150px;">')
print('<tr><th align="right" style="color:lightgray;">Recipt No. :</th>')
print('<td align="right"><input type="number" name="rn"></td></tr><tr>')
print('<th align="right" style="color:lightgray;">Student Name :</th>')
print('<td align="right"><input type="text" name="sn"></td>')
print('</tr><tr><th align="right" style="color:lightgray;">Addmission No. :</th>')
print('<td align="right"><input type="number" name="an"></td>')
print('<th align="right" style="color:lightgray;">Total Amout :</th>')
print('<td align="right"><input type="number" name="ta"></td>')
print('</tr><tr><th align="right" style="color:lightgray;">Date :</th>')
print('<td align="center"><input type="date" name="date"></td>')
print('<th align="right" style="color:lightgray;">Paid Amount :</th>')
print('<td align="right"><input type="number" name="pa"></td></tr><tr>')
print('<th align="right" style="color:lightgray;">Branch :</th>')
print('<td align="right"><input type="text" name="br"></td>')
print('<th align="right" style="color:lightgray;">Balance :</th>')
print('<td align="right"><input type="number" name="ba"></td></tr><tr>')
print('<th align="right" style="color:lightgray;">Semster:</th>')
print('<td align="right"><input type="number" name="se"></td></tr><tr><tr><tr></tr></tr></tr><tr>')
print('<th align="right"><input type="submit" name="sa" class="butt" value="SAVE"></th>')
print('<td align="right"><input type="reset" name="res" class="butt" value="RESET"></td>')
print('<td align="right"><a href="Homepage.html"><input type="button" name="ex" class="butt" value="EXIT"></input></a></td></tr></table>')
print('</form></div>')


print('<div style="background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT96UXWNYMMonDDFSXaNVO7ha-vOQb1It5aw&usqp=CAU); background-repeat: no-repeat; width: 500px; height:340px; float: right; margin-top: -300px; background-size:500px 340px;">')
print('<form action="" method="get">')
print('<Center><table style="font-size:30px; margin-top:100px; "><tr><th align="right" style="color:lightgray;">Recipt No. :</th>')
print('<td align="right"><input type="text" name="rc" style="height:30px; width:200px;"></td></tr>')
print('<tr><center><th><input type="submit" name="di" class="butt" value="SEARCH"></th></tr>')
print('</table></center></form></div></center><br><center>')
print('<div style="border-color: black; width:1200px; height: 100px; background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT96UXWNYMMonDDFSXaNVO7ha-vOQb1It5aw&usqp=CAU); background-repeat: no-repeat; background-size: 1200px 200px;">')
print("<table border='1'>")
print("<tr><th>recipt no</th><th>Student Name</th><th>addmision</th><th>total amount</th>")
print("<th>date</th><th>paid</th><th>branch</th><th>balance</th><th>semester</th</tr>")


ff=cgi.FieldStorage()

rn=ff.getvalue("rc")
conn=pymysql.Connection(host="localhost",password="",user="root",database="shree",port=3306)
cur=conn.cursor()
cur.execute("select * from fee where recipt_no=%s",(rn))
data=cur.fetchall()


for i in data:
    print("<tr><td>",i[0],"</td>")
    print("<td>",i[1],"</td>")
    print("<td>",i[2],"</td>")
    print("<td>",i[3],"</td>")
    print("<td>",i[4],"</td>")
    print("<td>",i[5],"</td>")
    print("<td>",i[6],"</td>")
    print("<td>",i[7],"</td>")
    print("<td>",i[8],"</td></tr>")
        
conn.commit()
print('</tr></table></div></center></body></html>')
