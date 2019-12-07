#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="market")

cursor=db.cursor();
flag=1

form=cgi.FieldStorage()
farmerid=form.getvalue("user")
username=form.getvalue("username")
password=form.getvalue("password")
marketid=None
results=[]
print("Content-type:text/html\r\n\r\n");
print("<html>")
try:
	sql="select marketname,location,marketid from admin"
	cursor.execute(sql)
	results=cursor.fetchall()
	#print(results)
except:
	print("something went wrong")
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



for i in results:
	print('''
			
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                   <a href=farmershow.py?marketid=%s> <div class="card">
                        <div class="card-image">'''%(i[2]))
	print('''	
                            <img src="logos/m4.jpg" style="width:100%;"/>
                        </div></a>
                        <div class="body">''')
	print('''name: %s<br>
						location:%s
						<br><a href="farmerrequest.py?user=%s&market=%s">
						<button type="submit">request</button></a>
						</div>
                    </div>
                </div>

                
                '''%(i[0],i[1],farmerid,i[2]))

print('''
</div>
            </div></section>

 <!-- Jquery Core Js -->
    <script src="plugins/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core Js -->
    <script src="plugins/bootstrap/js/bootstrap.js"></script>

    <!-- Select Plugin Js -->
    <script src="plugins/bootstrap-select/js/bootstrap-select.js"></script>

    <!-- Slimscroll Plugin Js -->
    <script src="plugins/jquery-slimscroll/jquery.slimscroll.js"></script>

    <!-- Waves Effect Plugin Js -->
    <script src="plugins/node-waves/waves.js"></script>

    <!-- Wait Me Plugin Js -->
    <script src="plugins/waitme/waitMe.js"></script>

    <!-- Custom Js -->
    <script src="js/admin.js"></script>
    <script src="js/pages/cards/colored.js"></script>

    <!-- Demo Js -->
    <script src="js/demo.js"></script>''')
print("</html>")