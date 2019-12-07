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
print("Content-type:text/html\r\n\r\n");

sellingrate=0;
print("<html>");




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
	
	
	</head>''')
print('''<body>
	<div class='slider'>
  <div class='slide1'></div>
  <div class='slide2'></div>
  <div class='slide3'></div>
</div>
   
	

          
	       



    </div>
    
  </nav>''')
try:
	
	sql="select * from `marketinfo` join `cropinfo` using(`cropid`) where `marketid`='%s'"%(marketid);
	cursor.execute(sql)
	results=cursor.fetchall()
		
		
	#print(results)
		
except:
	print("ërror here")
vegetables=[]
fruits=[]
crops=[]
for i in results:
	
	if i[4]=="vegetable":
		vegetables.append(i)
fruits=[]
for i in results:
	if i[4]=="fruit":
		fruits.append(i)
crops=[]
for i in results:
	if i[4]=="crop":
		crops.append(i)
#print(vegetables)
print('''

<div class="card">
                       
                        <div class="body">
						
<ul class="nav nav-tabs tab-nav-right" role="tablist">
                                <li role="presentation" class="active"><a href="#vegetables" data-toggle="tab">VEGETABLES</a></li>
                                <li role="presentation"><a href="#fruits" data-toggle="tab">FRIUTS</a></li>
                                <li role="presentation"><a href="#crops" data-toggle="tab">CROPS</a></li>
                            </ul>
							<div class="tab-content">
<div role="tabpanel" class="tab-pane fade in active" id="vegetables">

		<section class="content">
        <div class="container-fluid">
<div class="row clearfix">''')



if len(vegetables)==0:
	print("nothing found here")
	
else:
	for i in vegetables:
		try:
			sql="select sellingrate from selling where marketid='%s' and cropid='%s'"%(i[1],i[0])
			cursor.execute(sql)
			results=cursor.fetchall()
			sellingrate=results[0][0]
		except:
			print("something went wrong")
			
		print('''             <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="card-image">

                            <img src="logos/%s.jpg"'''%(i[3]))
		print('''style="width:100%;"/>''')
		print('''
                        </div>
                        <div class="body">
name: %s<br>
						rate:%s<br>
						selling rate:%s
						</div>
                    </div>
                </div>

                
                




'''%(i[3],i[2],sellingrate))

                                 
print('''</div>
            </div></section>
</div>
                            <div role="tabpanel" class="tab-pane fade " id="fruits">''')
							
print('''							<section class="content">
        <div class="container-fluid">
<div class="row clearfix">

''')



			
if len(fruits)==0:
	print("nothing found here")
	
else:
	for i in fruits:
		try:
			sql="select sellingrate from selling where marketid='%s' and cropid='%s'"%(i[1],i[0])
			cursor.execute(sql)
			results=cursor.fetchall()
			sellingrate=results[0][0]
		except:
			print("something went wrong")
		print('''             <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="card-image">

                            <img src="logos/%s.jpg"'''%(i[3]))
		print('''style="width:100%;"/>''')
		print('''
                        </div>
                        <div class="body">
name: %s<br>
						rate:%s<br>
						selling rate :%s
						</div>
                    </div>
                </div>

                
                




'''%(i[3],i[2],sellingrate))



print('''  </div>
            </div></section>

	</div>	
                                <div role="tabpanel" class="tab-pane fade" id="crops">''')
print('''							<section class="content">
        <div class="container-fluid">
<div class="row clearfix">

''')

if len(crops)==0:
	print("nothing found here")
	
else:
	for i in crops:
		try:
			sql="select sellingrate from selling where marketid='%s' and cropid='%s'"%(i[1],i[0])
			cursor.execute(sql)
			results=cursor.fetchall()
			sellingrate=results[0][0]
		except:
			print("something went wrong")
		print('''             <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="card-image">

                            <img src="logos/%s.jpg"'''%(i[3]))
		print('''style="width:100%;"/>''')
		print('''
                        </div>
                        <div class="body">
name: %s<br>
						rate:%s
						<br>
						selling rate:%s 
						</div>
                    </div>
                </div>

                
                




'''%(i[3],i[2],sellingrate))








print('''
</div>
</div></section>
<br><br>
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
	

	<a href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"/>
	<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Popper JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js">

	
	
</body></html>''');
