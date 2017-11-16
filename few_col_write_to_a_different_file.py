import csv 
import os

filename='/home/ayush/Desktop/xyz.csv'
with open(filename ,'rU') as f:
	reader=csv.reader(f)
	with open('/home/ayush/Desktop/out.csv','w') as e:
		rit=csv.writer(e)
		
		for row in reader:
			r=[]
			r.append(row[0])
			r.append(row[1])
			rit.writerow(r)



