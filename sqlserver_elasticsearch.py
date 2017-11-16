from elasticsearch import elasticsearch
from os import getenv
import pymssql
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
args = sys.argv
#ELASTICSEARCH CONNECTION
elasticsearchAddress = str(args[1])
index = str(args[2])
doc_type = str(args[3])
connES=Elasticsearch(elasticsearchAddress)
#SQL SERVER CONNECTION
server = "xxx.xxx.x.xxx:1433"
user = "sa"	
password = "XXXXXXXX"
database = "testing" 

conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()
cursor.execute('select * from table')
def return_dict_pair(row_item):
	return_dict = {}
	for column_name, row in zip(cursor.description, row_item):
		return_dict[column_name[0]] = row
	return return_dict

return_list = []

for row in cursor:
	row_item = return_dict_pair(row)
	return_list.append(row_item)
#print(cursor.fetchall())
a=0
for p in return_list:
	a=a+1
	res = connES.index(index=index, doc_type='doc_type', id=a, body=p)
print(res['created'])

# conn.close()
