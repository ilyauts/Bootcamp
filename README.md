Jesse’s Bootcamp

Go to https://dev.mysql.com/downloads/mysql/
Create Oracle account
Download Mac OS X 10.12 (x86, 64-bit), DMG Archive
Install the dmg that you just downloaded
Go to the drive and install the database
SAVE THE PASSWORD!!!!!!!!!!
Otherwise prepare to reinstall everything
Press “cmd + space” and type in “mysql”
Press “Start MySql Server”
Go to the terminal
Copy the following: PATH="/usr/local/mysql/bin:$PATH"
This lets the terminal know where you have executable binaries and allows you to type mysql in the terminal instead of /usr/local/mysql/bin/mysql
Type mysql -u root -p
Paste the password you saved and press enter
Congrats you got MySQL up!
Change your password ALTER USER 'root'@'localhost' IDENTIFIED BY 'admin';
Feel free to change admin to anything you prefer









Let’s explore the databases that we currently have: show databases;
Create a new database: create database bootcamp;
Check that it was created: show databases;
Select the database that you just created: use bootcamp;
See if there are any tables in the database: show tables;
There shouldn’t be any.
Let’s create one: CREATE TABLE first_table (name VARCHAR(20), AGE INTEGER);
In SQL column and tables names follow the underscore nomenclature
Check out some of the other datatypes here: https://dev.mysql.com/doc/refman/5.7/en/data-type-overview.html
Let’s query the table: SELECT * FROM first_table;
Notice that it’s empty because you haven’t added anything to it yet
Let’s add a row: INSERT INTO first_table (name, age) VALUES (“Jesse”, 24);
Query the table again: SELECT * FROM first_table;
You should now see what you stored in the table!
Let’s use a GUI
Downlod DB Visualizer here: https://www.dbvis.com/download/
Connect to your MySQL instance
Create a new connection to: localhost:3306
Username is: root
Password is whatever you made it


~~~ So you say you want to do data science eh? Let’s get some data! ~~~


Go to: https://www.data.gov/
Download some data, for example: http://www.ntsb.gov/investigations/data/Documents/datafiles/table10_2014.csv 
Rename the file to something sensible
Let’s create a table that will work with dataset
Go to DB Visualizer, on the top select bootcamp for the database
Then run the following query to create a table: CREATE TABLE oh_ohs (year INTEGER, injuries INTEGER, fatal_injuries INTEGER, total_fatalities INTEGER, fatalities_abroad INTEGER, flight_hours INTEGER, everything DOUBLE, fatal DOUBLE); 
Clean the table. 
 Get used to having to clean data!
 Remove the header rows, and all of the garbage on the bottom of the file.
 Select all of the integer values
 Right click
 Click format data
 Select ‘Number’ on the left side
 Set the precision at 0
 Save the file
You should now have another empty table
Test it by querying: SELECT * FROM oh_ohs;
Let’s import some data: LOAD DATA LOCAL INFILE '/Users/R594437/Downloads/data.csv' INTO TABLE oh_ohs FIELDS TERMINATED BY ',' ;
 Ensure that your query features your path / file name
See what you have:
 SELECT * FROM oh_ohs;
Let’s try a more complicated query:
 SELECT * FROM oh_ohs WHERE flight_hours > 20000000 AND (fatal_injuries * 2) < total_fatalities; 


~~~ SQL isn’t enough? Let’s have python do some number crunching! ~~~



Let’s create a python script: vim script.py
Let’s edit the script, press ‘i’, then paste the following:

import mysql.connector
from mysql.connector import errorcode

try:
  config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'bootcamp'
  }
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print 'Connected!'
  cnx.close()


Press ‘esc’
Type: :wq to save your work and press ‘enter’
For the script to run we need the packages that we import in the script to be installed
Determine which packages you can install on your version of the machine: pip search mysql-connector
This worked for me: pip install mysql-connector
Now run the script: python script.py




~~~ Are you an all-Dstar who got this far? Well that’s all that I prepared in 4 hours, please read the link below for more! ~~~

http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

