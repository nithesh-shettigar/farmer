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
results=[]
results1=[]
flag=1
marketname=""
cropname=""
location=""
print("Content-type:text/html\r\n\r\n");
print("<html>")
print('''
<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">
 <script type="text/javascript" src="gstatic/loader.js"></script>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Tabs | Bootstrap Based Admin Template - Material Design</title>
    <!-- Favicon-->
    <link rel="icon" href="../../favicon.ico" type="image/x-icon">

    <!-- Google Fonts -->
    <link href="latin,cyrillic-ext.css" rel="stylesheet" type="text/css">
    <link href="Material+Icons.css" rel="stylesheet" type="text/css">

    <!-- Bootstrap Core Css -->
    <link href="plugins/bootstrap/css/bootstrap.css" rel="stylesheet">

    <!-- Waves Effect Css -->
    <link href="plugins/node-waves/waves.css" rel="stylesheet" />

    <!-- Animation Css -->
    <link href="plugins/animate-css/animate.css" rel="stylesheet" />

    <!-- Custom Css -->
    <link href="css/style.css" rel="stylesheet">

    <!-- AdminBSB Themes. You can choose a theme from css/themes instead of get all themes -->
    <link href="css/themes/all-themes.css" rel="stylesheet" />
</head>
<style>
.c1{
width=100% absolute;
}
</style>

<body><section class="content">
        <div class="container-fluid">
<div class="row clearfix">
''')
try:
	sql="Select * from farmerinfo where farmerid='%s'"%(farmerid)
	cursor.execute(sql)
	results=cursor.fetchall()
except:
	print("something went wrong1")
for i in results:
	try:
		sql="select name from cropinfo where cropid='%s'"%(i[0])
		cursor1.execute(sql)
		cropname=cursor1.fetchall()[0][0]
	except:
		print("something went wrong2")
	print('''
			
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="card-image">''')
	print('''	
                            <img src="logos/%s.jpg" '''%(cropname))
	print('''style="width:100%;"/>
                        </div></a>
                        <div class="body">''')
	print('''name: %s<br>
						acres:%s
						
						</div>
                    </div>
                </div>

                
                '''%(cropname,i[1]))
print("</body>")
print("</html>")
	



