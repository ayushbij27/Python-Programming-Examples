# -*- coding: utf-8 -*-
import random
import uuid
import csv
from datetime import date,timedelta


header = ['Brand','Locations','Gender','Category','Age_Group,','curr_ror','Curr_prr','Date']


myfile = open('Generated3.csv','w+')
wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)
wr.writerow(header)


Gender = ['Male','Female']
Age_Group = ['18-30','30-45','45-60','60+'] 
Category = ['Skincare','Eyeliner','colossal kajal','Lipstick','Shampoo']
Locations = ['East America','North America','South America','West America']
Brand = [
                'Pond\'s',
                'Vaseline',
                'Amway',
                'Pantene',
                'Head & Shoulders',
                'Lakme',
                'Maybelline',
                'Loreal',
                'Meilin',
]

for brand in Brand:
    base = date(2016,1,1)
    Date_List = [base-timedelta(days=x) for x in range(0,365)]
    for Date in Date_List:
        location =random.choice(Locations)
        gender= random.choice(Gender)
        category = random.choice(Category)
        age_group = random.choice(Age_Group)
        curr_ror = round(random.uniform(0,2),6)
        Curr_prr = round(random.uniform(0,2),6) 
        a_list=[brand,location,gender,category,age_group,curr_ror,Curr_prr,Date]
        
        # myfile = open('Generated3.csv','w+')
        # wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)
        wr.writerow(a_list)
myfile.close()

    
