import os 
import sys

a=["This is a longest sentence","where are you","What is your name"]

b=[word for sublist in a for word in sublist.split()]

max_value=len(b[0])

word=b[0]
for i in b:
	if(len(i)>max_value):
		max_value=len(i)
		word=i
print max_value

print word