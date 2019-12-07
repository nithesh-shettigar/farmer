#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="market")

cursor=db.cursor();
flag=1
form=cgi.FieldStorage()
marketid=form.getvalue("m")
cropid=form.getvalue("c")
results=[]
print("Content-type:text/html\r\n\r\n");
print(''' 
 <head>
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

print("<html>");
try:
	
	sql="select * from `marketinfo` join `cropinfo` using(`cropid`) where marketid='%s' and marketinfo.cropid='%s'"%(marketid,cropid);
	cursor.execute(sql)
	results=cursor.fetchall()
		
		
	#print(results)
		
except:
	print("ërror here")
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

<form action="marketupdateinfovaluesdone.py?m=%s&c=%s" method="post" id="login-form"><input type="hidden" name="csrfmiddlewaretoken" value="N3XJ80FkKF6aUL7mfTzg1dc6pmhTZ6gOZ1Vh0qEE0Z6MLUEwwSzo49UAStYbiHnl">
  <div class="form-row">
    
    <label class="required" for="id_username">item:</label> <input type="text" name="item autofocus required id="id_username" value=%s disabled="disabled"> 
  </div>
 <div class="form-row">
    
    <label class="required" for="id_username">type:</label> <input type="text" name="type" autofocus required id="id_username" value=%s disabled="disabled">
  </div>
  <div class="form-row">
    
    <label class="required" for="id_username">current rate/unit:</label> <input type="text" name="current" autofocus required id="id_username" value=%d disabled="disabled">
  </div>
  <div class="form-row">
    
    <label class="required" for="id_username">add new rate:</label> <input type="text" name="new" autofocus required id="id_username">
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

</body>'''%(marketid,cropid,results[0][3],results[0][4],results[0][2]))
print("</html>")