#!C:\Users\HP\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
import mysql.connector
cgitb.enable();

db=mysql.connector.connect(user="root",password="",host="localhost",database="farmer")
db1=mysql.connector.connect(user="root",password="",host="localhost",database="market")

cursor=db.cursor();
cursor1=db1.cursor();

flag=1
r=[]
cropname=None
graphland=[]
graphlog=[]
graphmarket=[]
marketname=None
form=cgi.FieldStorage()
username=form.getvalue("username")
password=form.getvalue("password")
faremrid=None
status=''
print("Content-type:text/html\r\n\r\n");

try:
	sql="select * from `farmeraccount` where username='%s' and password='%s'"%(username,password)
	cursor.execute(sql)
	results=cursor.fetchall()
	if len(results)==0:
		flag=0
		print("äccount not found")
	else:
		farmerid=results[0][0]
		
except:
	print("ërror")
try:
	sql="select * from log where farmerid='%s'"%(farmerid)
	cursor.execute(sql)
	graphlog=cursor.fetchall()
except:
	print("error")
try:
	sql="select * from farmerinfo  where farmerid='%s'"%(farmerid)
	cursor.execute(sql)
	graphland=cursor.fetchall()
	#print(graphland)
except:
	print("error")
try:
	sql="select * from farmerinfo where farmerid='%s'"%(farmerid)
	cursor1.execute(sql)
	graphmarket=cursor1.fetchall()
except:
	print("error graphmarket")
	
	
print('''<html>
<head>
<link rel="stylesheet" href="all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">
<link href="latin,cyrillic-ext" rel="stylesheet" type="text/css">
    <link href="Material+Icons" rel="stylesheet" type="text/css">
    <script type="text/javascript" src="gstatic/loader.js"></script>

    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>farmer</title>
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

<script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
	        google.charts.setOnLoadCallback(drawChart1);
google.charts.setOnLoadCallback(drawChart2);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],''')
for i in graphland:
	try:
		sql="select name  from cropinfo where cropid='%s'"%(i[0])
		cursor1.execute(sql)
		cropname=cursor1.fetchall()[0][0]
	except:
		print("error")
	print('''
          ['%s',     %d],'''%(cropname,int(i[1])))
          
print('''
]); var options = {
          title: 'land share of crops',
          is3D: true,
		  backgroundColor:'#DCDCDC',
        };
var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);}

		
		 function drawChart1() {
        var data1 = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],''')
for i in graphlog:
	try:
		sql="select name  from cropinfo where cropid='%s'"%(i[0])
		cursor1.execute(sql)
		cropname=cursor1.fetchall()[0][0]
	except:
		print("error")
	print('''
          ['%s',     %f],'''%(cropname,float(i[2])))
          
print('''
]); var options1 = {
          title: 'profit share of crops',
          is3D: true,
		  backgroundColor:'#DCDCDC',
        };
var chart1 = new google.visualization.PieChart(document.getElementById('piechart_3d1'));
        chart1.draw(data1, options1);}

		
function drawChart2() {
        var data2 = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],''')

for i in graphmarket:
	print('''         ['%s',     %f],'''%(i[2],i[1]))

print('''         
        ]);

        var options2 = {
          title: 'profit by market',
          is3D: true,
		   backgroundColor:'#DCDCDC'
        };

        var chart2 = new google.visualization.PieChart(document.getElementById('piechart_3d3'));
        chart2.draw(data2, options2);
      }
    </script>


''')


try:
	sql="select * from farmernotifications where farmerid='%s'"%(farmerid)
	cursor.execute(sql)
	r=cursor.fetchall()
	#print(r)
except:
	print("error")
print('''

 <body class="theme-green"  bgcolor="#32CD32">
 <nav class="navbar">
        <div class="container-fluid">
            <div class="navbar-header">
                <a href="javascript:void(0);" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse" aria-expanded="false"></a>
                <a href="javascript:void(0);" class="bars"></a>
                <a class="navbar-brand" href="index.html">ADMINBSB - MATERIAL DESIGN</a>
            </div>
			</div>
			            <div class="collapse navbar-collapse" id="navbar-collapse" style="width:100%;">
                <ul class="nav navbar-nav navbar-right">
                    <!-- Call Search -->
                    <!-- #END# Call Search -->
                    <!-- Notifications -->
                    <li class="dropdown">
                        <a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button">
                            <i class="material-icons">notifications</i>
                            <span class="label-count"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li class="header">NOTIFICATIONS</li>
                            <li class="body">
                                <ul class="menu">''')
for i in r:
	try:
		sql="select name from cropinfo where cropid='%s'"%(i[3])
		cursor1.execute(sql)
		cropname=cursor1.fetchall()[0][0]
	except:
		print("something went wrong1")
	try:
		sql="select marketname from admin where marketid='%s'"%(i[1])
		cursor1.execute(sql)
		marketname=cursor1.fetchall()[0][0]
	except:
		print("something went wrong1")
	status=i[2]+"ed"
		
	print('''
                                                       
                                    
                                    
                                    
                                    <li>
                                        <a href="javascript:void(0);">''')
	if i[2]=="accept":
		print('''
                                            <div class="icon-circle bg-light-green"><i class="material-icons">thumb_up</i>
                                            </div>''')
	else:
		print('''
                <div class="icon-circle bg-red"><i class="material-icons">thumb_down</i>
                                            </div>''')
	
	print('''			
                                            <div class="menu-info">''')
											
	print('''						<h4><b></b> </h4>	<h4>			
                                                %s%d,%d %s by %s
                                               </h4>
                                            </div>
                                        </a>
                                    </li>'''%(cropname,int(i[4]),int(i[5]),status,marketname))
                                   
print('''                               </ul>
                            </li>
                            <li class="footer">
                                <a href="javascript:void(0);">View All Notifications</a>
                            </li>
                        </ul>
                    </li>
                    <!-- #END# Notifications -->
                    
                    <!-- #END# Tasks -->
                </ul>
            </div>
			</nav><br><br><br><br><br><br><br>
''')






if flag==1:
	print('''
	 <div class="row clearfix">
		<div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
			
    <div id="piechart_3d"  ></div>
</div>

<div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
			
    <div id="piechart_3d1"  ></div>
</div>
<div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
			
    <div id="piechart_3d2"  ></div>
</div>

<div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
			
    <div id="piechart_3d3"  ></div>
</div>


</div><br>
 <div class="row clearfix">
                

 
                <div class="col-lg-4  col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-green">
                            <h2>
                                Update YOUR information here
                            </h2>
                            
                        </div>
                        <div class="body bg-green"><a href="farmerupdate.py?user=%s">'''%(farmerid))
						
	print('''						<img src="logos/update.jpg" style="height:50%;width:100%;"/></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-green">
                            <h2>
                              see your informations
                            </h2>
                           
                        </div>''')
	print('''
                        <div class="body bg-green"><a href="farmerinfo.py?user=%s">'''%(farmerid))
	print('''
                          <img src="logos/farmer1.jpg" style="height:50%;width:100%;"/></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-green">
                            <h2>
                                see market informations here
                            </h2>
                            
                        </div>''')
	print('''
                        <div class="body bg-green"><a href="farmermarketinfo.py?user=%s">'''%(farmerid))
	print('''
                          <img src="logos/market2.jpg" style="height:50%;width:100%;"/></a> </div>
                    </div>
                </div>
				<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header bg-green">
                            <h2>
                                see vehicle informations here
                            </h2>
                            
                        </div>''')
	print('''
                        <div class="body bg-green"><a href="farmervehicleinfo.py?user=%s">'''%(farmerid))
	print(''' <img src="logos/small.jpg" style="height:50%;width:100%;"/></a> </div>
                    </div>
            </div>
''')
print('''		 <!-- Jquery Core Js -->
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
			
</body>''');
print("</html>");
