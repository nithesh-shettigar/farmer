#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="farmer")
db1=mysql.connector.connect(user="root",password="",host="localhost",database="market")
cursor=db.cursor();
cursor1=db1.cursor();
flag=1
form=cgi.FieldStorage()
farmerid=form.getvalue("user")
crop=form.getvalue("crops")
cropid=None
marketid=form.getvalue("market")
acre=form.getvalue("acre")
results=[]
results1=[]
flag=1
marketname=""
location=""
print("Content-type:text/html\r\n\r\n");