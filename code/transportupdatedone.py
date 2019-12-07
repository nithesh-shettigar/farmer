#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="transport")
cursor=db.cursor();
flag=1
form=cgi.FieldStorage()
ownerid=form.getvalue("user")
cropid=None
vehiclecount=form.getvalue("vehiclecount")
results=[]
vehicletype=form.getvalue("vehicle")
results1=[]
results=[]
flag=1
marketname=""
location=""
print("Content-type:text/html\r\n\r\n");
print("<html>")
print('''
<head><meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>No Header Card | Bootstrap Based Admin Template - Material Design</title>
    <!-- Favicon-->
    

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&subset=latin,cyrillic-ext" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type="text/css">

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
  
  
  
  
  
  
  
  
  
  
  
  
  
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="msapplication-tap-highlight" content="no">
    <meta name="description" content="Materialize is a modern responsive CSS framework based on Material Design by Google. ">
    <title>Documentation - Materialize</title>
    <!-- Favicons-->

    <link rel="apple-touch-icon-precomposed" href="apple-touch-icon-152x152.png">
    <meta name="msapplication-TileColor" content="#FFFFFF">
    <meta name="msapplication-TileImage" content="mstile-144x144.png">
    <link rel="icon" href="favicon-32x32.png" sizes="32x32">
    <!--  Android 5 Chrome Color-->
    <meta name="theme-color" content="#EE6E73">
    <!-- CSS-->
    <link href="prism.css" rel="stylesheet">
       <link href="ghpages-materialize.css" type="text/css" rel="stylesheet" media="screen,projection">

    <link href="farmerlogo1.css" rel="stylesheet" type="text/css">
    <link href="farmerlogo2.css" rel="stylesheet">
    <!-- if !isDemo-->
    <!--   script.-->
    <!--     window.liveSettings = {-->
    <!--       api_key: "a0b49b34b93844c38eaee15690d86413",-->
    <!--       picker: "bottom-right",-->
    <!--       detectlang: true,-->
    <!--       dynamic: true,-->
    <!--       autocollect: true-->
    <!--     };-->
    <!--   script(src='//cdn.transifex.com/live.js')-->
  </head>

<body>''')
try:
	sql="select vehicleid from vehicle where type='%s'"%(vehicletype)
	cursor.execute(sql)
	results=cursor.fetchall()
except:
	print("something went wrong")
	
try:
	sql="select * from ownerinfo where ownerid='%s' and vehicleid='%s'"%(ownerid,results[0][0])
	cursor.execute(sql)
	results1=cursor.fetchall()
	if len(results1)==0:
		try:
			sql="insert into ownerinfo values('%s','%s','%d')"%(ownerid,results[0][0],int(vehiclecount))
			cursor.execute(sql)
			db.commit()
		except:
			print("something went wrong")
	else:
		try:
			sql="update ownerinfo set noofvehicle=noofvehicle+'%d' where vehicleid='%s' and ownerid='%s' "%(int(vehiclecount),results[0][0],ownerid)
			cursor.execute(sql)
			db.commit()
		except:
			print("something went wrong")
except:
	print("something is wrong here")
print('''<center>


 <div class="alert alert-warning alert-dismissible" role="alert">
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
insertion done  successfully                      </div>
<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12" style="margin:100;" >
                    <div class="card">
                        <div class="body light-green">
						<div class="card-image">
						<img src="logos/tick2.jpg">
                        </div>
						<br><br>
						
						</div>
                    </div>
                </div>


</center>''')
print("</body></html>")

	