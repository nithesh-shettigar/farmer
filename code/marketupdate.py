#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="market")

cursor=db.cursor();
flag=1
form=cgi.FieldStorage()
marketid=form.getvalue("user")
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
	sql="select name from cropinfo where 1";
	cursor.execute(sql)
	results=cursor.fetchall()
		
		
	#print(results)
except:
	print("ërror")
	
try:
	sql="select marketname,location from admin where marketid='%s'"%(marketid)
	cursor.execute(sql)
	results1=cursor.fetchall()
	marketname=results1[0][0]
	location =results1[0][1]
		
	#print(results1)
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

<form  action="marketupdatedone.py?user=%s" method="post" id="login-form"><input type="hidden" name="csrfmiddlewaretoken" value="N3XJ80FkKF6aUL7mfTzg1dc6pmhTZ6gOZ1Vh0qEE0Z6MLUEwwSzo49UAStYbiHnl">
  <div class="form-row">
    
    <label class="required" for="id_username">marketname:</label> <input type="text" name="marketname" autofocus required id="id_username" value=%s > 
  </div>
 <div class="form-row">
    
    <label class="required" for="id_username">location:</label> <input type="text" name="location" autofocus required id="id_username" value=%s >
  </div>'''%(marketid,marketname,location))
print('''
  <div class="form-row">
    
<div class="col-sm-6">
                                  
								  <select class="form-control show-tick" name="crops">
    <option value="">-- Please select --</option>''')
	
for i in results:
		print('''<option value="%s">%s</option>'''%(i[0],i[0]))
	
	
	

print('''
		</select>
                                </div>  </div>
  <br>
  <div class="form-row">
    
    <label class="required" for="id_username">add rate</label> <input type="text" name="rate" autofocus required id="id_username">
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