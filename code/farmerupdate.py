#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db1=mysql.connector.connect(user="root",password="",host="localhost",database="market")
db2=mysql.connector.connect(user="root",password="",host="localhost",database="farmer")

cursor1=db1.cursor();
cursor2=db2.cursor();

flag=1
form=cgi.FieldStorage()
farmerid=form.getvalue("user")
results=[]
results1=[]
marketname=""
location=""
print("Content-type:text/html\r\n\r\n");
print("<html>")
print(''' <head>




 <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Basic Form Elements | Bootstrap Based Admin Template - Material Design</title>
    <!-- Favicon-->
    <link rel="icon" href="../../favicon.ico" type="image/x-icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&subset=latin,cyrillic-ext" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type="text/css">

    <!-- Bootstrap Core Css -->
    <link href="plugins/bootstrap/css/bootstrap.css" rel="stylesheet">

    <!-- Waves Effect Css -->
    <link href="plugins/node-waves/waves.css" rel="stylesheet" />

    <!-- Animation Css -->
    <link href="plugins/animate-css/animate.css" rel="stylesheet" />

    <!-- Bootstrap Material Datetime Picker Css -->
    <link href="plugins/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css" rel="stylesheet" />

    <!-- Wait Me Css -->
    <link href="plugins/waitme/waitMe.css" rel="stylesheet" />

    <!-- Bootstrap Select Css -->
    <link href="plugins/bootstrap-select/css/bootstrap-select.css" rel="stylesheet" />

    <!-- Custom Css -->
    <link href="css/style.css" rel="stylesheet">

    <!-- AdminBSB Themes. You can choose a theme from css/themes instead of get all themes -->
    <link href="css/themes/all-themes.css" rel="stylesheet" />











	<link rel="stylesheet" href="materialize.min.css">



    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>some title</title>
    <!-- Favicon-->

    <!-- Google Fonts -->
    <link href="latin,cyrillic-ext.css" rel="stylesheet" type="text/css">
    <link href="Material+Icons.css" rel="stylesheet" type="text/css">

    <!-- Bootstrap Core Css -->
   
  <link rel="stylesheet" type="text/css" href="base.css">
<link rel="stylesheet" type="text/css" href="login.css">
  <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <link rel="stylesheet" type="text/css" href="responsive.css">
    
      <!--Let browser know website is optimized for mobile-->
     <meta name="MobileOptimized" content="320">
                <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<style>
div.cities {
        background-color:white;
    color: black;
   

} 


div.cities1 {
    background-color:green;
    color: white;
   
} </style>
''')
try:
	sql="select * from cropinfo ";
	cursor1.execute(sql)
	results=cursor1.fetchall()
	
except:
	print("ërror")
print('''
<body class=" login"
  data-admin-utc-offset="0">

<!-- Container -->
<div id="container">

    
    <!-- Header -->
    <div id="header">
        <div id="branding">
        
<h1 id="site-name"><a href="#">market login</a></h1>

        </div>
        
        
    </div>
    <!-- END Header -->
    <!-- Content -->
    <div id="content" class="colM">   

<div id="content-main">

<form  action="farmerupdatedone.py?user=%s" method="post" id="login-form"><input type="hidden" name="csrfmiddlewaretoken" value="N3XJ80FkKF6aUL7mfTzg1dc6pmhTZ6gOZ1Vh0qEE0Z6MLUEwwSzo49UAStYbiHnl">
 

  <div class="form-row">
    
<div class="col-sm-6">
                <label class="required" for="id_username" >choose field item</label><br>                 
								  <select class="form-control show-tick" name="crops">
 '''%(farmerid))
	
for i in results:
		print('''<option value="%s">%s</option>'''%(i[1],i[1]))

print('''
		</select>
                                </div>  </div>
  <br>
  <div class="form-row">
    
    <label class="required" for="id_username">acres</label> <input type="text" name="acre" autofocus required id="id_username">
  </div>
 
  
  
  <div class="submit-row">
    <label>&nbsp;</label><input type="submit" value="submit">
  </div>
</form>

</div>

        
        <br class="clear">
    </div>
    <!-- END Content -->

    <div id="footer"></div>
</div>
<!-- END Container -->

</body>
''')
print("</html>")
	