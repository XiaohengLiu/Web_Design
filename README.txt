Introduction:
  This is a very simple website to do the stock searching, prediction and some other basic function about web pages like user login. I built this in order to practice what I have learnt about HTML/CSS, JavaScript/Jquery, Python/Django

System: Deepin linux 2013

Script:Python

Framework:Django

Front-end:HTML,CSS,Jquery

Database:SQLite3

python-library:	Pandas
, Matplotlib
, django
, numpy


File 

structure:
	
+-------+---->Web			//readme etc
		
+------->stockapp		//everyting background
			+------->stocksys	//Framework files
			
+------->manage.py	//use to manage the whole project
			+------->stockapp	//All setting files
		
+------->template		//everything front-end
			+------->css		//css files
			
+------->js		//javascript files
			
+------->images		//images

Compile instruction:
	

IF YOU WANT TO RUN THE CODE, MAKE SURE YOU HAVE EVERY THING BACKGROUND

	MAKE SURE CHANGE SETTINGS IN STOCKAPP TO CHANGE THE STATIC DIRECTORY

	RUN COMMAND
		$python manage.py runserver

		$firefox

		TYPE IN THE ADDRESS 127.0.0.1:8000/index/

