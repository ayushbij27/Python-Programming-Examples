# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json
from urllib2 import Request, urlopen, URLError
import time
import csv
import codecs
# try:
response = requests.get("http://www.restcountries.eu/rest/v2/all")
print(response.status_code)
data_list=[]
data_list = json.loads(response.text)
list_data=[]
	

# data_list=[{"name":"Afghanistan",
# "topLevelDomain":[".af"],
# "alpha2Code":"AF",
# "alpha3Code":"AFG",
# "callingCodes":["93"],
# "capital":"Kabul",
# "altSpellings":["AF","Afġānistān"],
# "region":"Asia",
# "subregion":"Southern Asia",
# "population":27657145,
# "latlng":[33.0,
# 65.0],
# "demonym":"Afghan",
# "area":652230.0,
# "gini":27.8,
# "timezones":["UTC+04:30"],
# "borders":["IRN","PAK","TKM","UZB","TJK","CHN"],
# "nativeName":"افغانستان",
# "numericCode":"004",
# "currencies":[{"code":"AFN","name":"Afghan afghani","symbol":"؋"}],
# "languages":[{"iso639_1":"ps","iso639_2":"pus","name":"Pashto","nativeName":"پښتو"},{"iso639_1":"uz","iso639_2":"uzb","name":"Uzbek","nativeName":"Oʻzbek"},{"iso639_1":"tk","iso639_2":"tuk","name":"Turkmen","nativeName":"Türkmen"}],
# "translations":{"de":"Afghanistan","es":"Afganistán","fr":"Afghanistan","ja":"アフガニスタン","it":"Afghanistan","br":"Afeganistão","pt":"Afeganistão"},
# "flag":"https://restcountries.eu/data/afg.svg",
# "regionalBlocs":[{"acronym":"SAARC","name":"South Asian Association for Regional Cooperation","otherAcronyms":[],"otherNames":[]}]
# }]
header = ['name','topLevelDomain','alpha2Code','alpha3Code','callingCodes','capital','altSpellings','region','subregion','population','latlng','demonym','area','gini','timezones','borders','nativeName','numericCode','currencies','languages','translations','flag']
# header = ",".join(header)
list_data.append(header)
myfile = open('data.csv','w+')
wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)

for i in data_list:
	callingcodes=""
	if len(i["callingCodes"])!=0:
		callingcodes=i["callingCodes"][0]
	list_data.append([i["name"],i["topLevelDomain"][0],i["alpha2Code"],i["alpha3Code"],
	callingcodes,
	i["capital"] ,
	"~".join(i["altSpellings"]) ,
	str(i["region"]) ,
	str(i["subregion"]) ,
	str(i["population"]) ,
	"~".join(str(i["latlng"])) ,
	i["demonym"] ,
	str(i["area"]) ,
	str(i["gini"]) ,
	"~".join(i["timezones"]) ,
	"~".join(i["borders"]) ,
	i["nativeName"] ,
	i["numericCode"] ,
	 # "~".join([(i["currencies"][0]["code"]),(i["currencies"][0]["name"]),(i["currencies"][0]["symbol"])]) ,
	# i["languages"] ,
	i["translations"]["de"] ,
	i["flag"]])
	

print(len(list_data))
print(list_data[1])
for i in list_data:
	wr.writerow(i)

	
	 	# # list_data.append(data_list)
	 	# with open('data.csv', 'w') as outfile:
	 	# 	json.dump(list_data, outfile)
		# print(list_data)	
# except:
# 	print "Unable to connect"	
