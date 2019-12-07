#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="transport")
cursor=db.cursor();
flag=1
form=cgi.FieldStorage()
ownerid=form.getvalue("user")
results=[]
results1=[]
image1=""
cost=""
capacity=""
flag=1
marketname=""
cropname=""
location=""
print("Content-type:text/html\r\n\r\n");
print("<html>")
print('''
<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">

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
	sql="Select * from ownerinfo where ownerid='%s'"%(ownerid)
	cursor.execute(sql)
	results=cursor.fetchall()
	#print(results)
except:
	print("something went wrong1")
for i in results:
	try:
		sql="select * from vehicle where vehicleid='%s'"%(i[1])
		cursor.execute(sql)
		results1=cursor.fetchall()
		#print(results1)
		image1=results1[0][2]
		cost=results1[0][1]
		capacity=results1[0][3]
	except:
		print("something went wrong")
	print('''
			
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="card-image">''')
	print('''	
                            <img src="logos/%s.jpg" '''%(image1))
	print('''style="width:100%;"/>
                        </div></a>
                        <div class="body">''')
	print('''type: %s<br>
						count:%s
						<br>
						cost:%s
						<br>
						capacity:%s
						</div>
                    </div>
                </div>

                
                '''%(image1,i[2],cost,capacity))
print("</body>")
print("</html>")
	



