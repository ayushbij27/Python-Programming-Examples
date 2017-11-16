# -*- coding: utf-8 -*-
from flask import Flask,make_response
import random
import uuid
import csv
from datetime import date,timedelta

app = Flask(__name__)


@app.route("/hello")
def hello():
	return "Hello"
@app.route("/", methods=['GET'])
def calling():
    header = ['Brand','Locations','Gender','Category','Age_Group','curr_ror','Curr_prr','Date']
    header = ",".join(header)
    
    # myfile = open('Generated3.csv','w+')
    # wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)
    # wr.writerow(header)
    
    
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
    a=[]
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
            a_list=brand+","+location+","+gender+","+category+","+age_group+","+str(curr_ror)+","+str(Curr_prr)+","+str(Date)
            a.append(a_list)
            # myfile = open('Generated3.csv','w+')
            # wr = csv.writer(myfile,quoting = csv.QUOTE_ALL)
            # wr.writerow(a_list)
    a.insert(0,header)
    b = "\n".join(a)        
    response = make_response(b)
    
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response

    myfile.close()


if __name__ == "__main__":
    app.run()
    

