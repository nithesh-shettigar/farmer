#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="market")

cursor=db.cursor();
flag=1
marketid=None
form=cgi.FieldStorage()
username=form.getvalue("username")
password=form.getvalue("password")
results=[]
marketid=None
print("Content-type:text/html\r\n\r\n");

try:
	sql="select * from `admin` where username='%s' and password='%s'"%(username,password)
	cursor.execute(sql)
	results=cursor.fetchall()
	if len(results)==0:
		flag=0
		print("äccount not found")
		
except:
	print("ërror")
print("<html>");


if flag==1:
	#print("account found")
	try:
		sql="select `marketid` from `admin` where username='%s' "%(username)
		cursor.execute(sql)
		results=cursor.fetchall()
		#print(results[0][0])
		marketid=results[0][0]
	except:
		print("ërror")
	print('''
	<html>

<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">

    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>market</title>
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

	<style >
	
	.slider {
  max-width: 1300px;
  height: 300px;
  margin: 20px auto;
  position: relative;
}
.slide1,.slide2,.slide3,.slide4,.slide5 {
  position: absolute;
  width: 100%;
  height: 100%;
}
.slide1 {
  background: url(logos/m1.jpg)no-repeat center;
      background-size: cover;
    animation:fade 8s infinite;
-webkit-animation:fade 8s infinite;

} 
.slide2 {
  background: url(logos/m2.jpg)no-repeat center;
      background-size: cover;
    animation:fade2 8s infinite;
-webkit-animation:fade2 8s infinite;
}
.slide3 {
    background: url(logos/m4.jpg)no-repeat center;
      background-size: cover;
    animation:fade3 8s infinite;
-webkit-animation:fade3 8s infinite;
}
.slide4 {
    background: url(logos/m3.jpg)no-repeat center;
      background-size: cover;
    animation:fade3 8s infinite;
-webkit-animation:fade3 8s infinite;
}
@keyframes fade
{
  0%   {opacity:1}
  33.333% { opacity: 0}
  66.666% { opacity: 0}
  100% { opacity: 1}
}
@keyframes fade2
{
  0%   {opacity:0}
  33.333% { opacity: 1}
  66.666% { opacity: 0 }
  100% { opacity: 0}
}
@keyframes fade3
{
  0%   {opacity:0}
  33.333% { opacity: 0}
  66.666% { opacity: 1}
  100% { opacity: 0}
}
	

div.cities {
        background-color:white;
    color: black;
   

} 


div.cities1 {
    background-color:green;
    color: white;
   
} 
</style>


 
<div class='slider'>
  <div class='slide1'></div>
  <div class='slide2'></div>
  <div class='slide3'></div>
</div>''')
	print('''
<div class="row clearfix">
                <div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-red">
                            <h2>
                                requests
                            </h2>
                            
                        </div>
                        <div class="body"><a href="marketnotification.py?market=%s">'''%(marketid))
	print('''	<img src="logos/request.jpg" style="height:50%;width:100%;"/></a>
                        </div>
                    </div>
                </div>''')					
						
	print('''


                <div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-red">
                            <h2>
                                Update market information here
                            </h2>
                            
                        </div>
                        <div class="body"><a href="marketupdate.py?user=%s">'''%(marketid))
						
	print('''						<img src="logos/update.jpg" style="height:50%;width:100%;"/></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-cyan">
                            <h2>
                              see farmer informations
                            </h2>
                           
                        </div>''')
	print('''
                        <div class="body"><a href="marketfarmerinfo.py?user=%s">'''%(marketid))
	print('''
                          <img src="logos/farmer1.jpg" style="height:50%;width:100%;"/></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-green">
                            <h2>
                                see your market rates here
                            </h2>
                            
                        </div>''')
	print('''
                        <div class="body"><a href="marketinfo.py?user=%s">'''%(marketid))
	print('''
                          <img src="logos/market2.jpg" style="height:50%;width:100%;"/></a> </div>
                    </div>
                </div>
            </div>
''')

			
	print('''		
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
    <script src="js/demo.js"></script>
			
</body>
</html>


''')