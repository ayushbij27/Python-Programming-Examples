import time
start_time = time.time()
from os import getenv
import pymssql
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
args = sys.argv
server = "xxx.xxx.x.xxx:1433"
user = "sa"
password = "#####"
database = "testing"

conn = pymssql.connect(server, user, password, database,autocommit = True)
cursor = conn.cursor()

a = """
___________________________________________________________

**********Select the operation to be performed*************
___________________________________________________________
1) Retrieve Data
2) Delete Table
3) Insert Data
"""
print(a)
num= raw_input("Enter the number : ")


	
if num=="1":
	while 1:
		print "Executing %s" %num 
		cursor.execute("select * from table ")
		
		print(cursor.fetchall())
		
		#conn.close()
	
elif num == "2":
		print  "Executing %s" %num 
		cursor.execute("delete from  table")
		#print(cursor.fetchall())
		#conn.close()
	
else:

		print  "Executing %s" %num 
		cursor.execute("insert into table (name,class) values('aakash','SD')")
		print(cursor.fetchall())
		#conn.close()
	
print("--- %s seconds ---" % (time.time() - start_time))