import os
import sys
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


from nltk.stem.snowball import SnowballStemmer


file = open('/home/ayush/Desktop/textmining' ,'r') 
# print file.read()
# string_list=[]
string_list=file.read()
print string_list
print len(string_list)
vectorizer = CountVectorizer(lowercase = True, stop_words = "english")
a=vectorizer.fit_transform(string_list)
print a

# stemmer=SnowballStemmer('english')
# a=stemmer.stem(string_list)
# print a
