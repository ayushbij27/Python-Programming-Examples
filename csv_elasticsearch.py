import csv 
import os
import sys
import time
from elasticsearch import helpers,Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# line_count=0	

filename='/home/ayush/Desktop/xyz.csv'
with open(filename,'rU') as csv_file:
	data_file=csv.DictReader(csv_file)

	helpers.bulk(es,data_file,index='ayush-2',doc_type='my-type')
# 	for row in data_file:
# 		line_count=line_count+1
# 		# print row
# print line_count
