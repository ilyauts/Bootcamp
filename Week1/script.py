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
