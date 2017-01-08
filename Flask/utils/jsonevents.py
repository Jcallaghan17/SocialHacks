'''details:
ends:
location: {
    lat:
    lng:
}
starts:
title:
'''
import sqlite3
import time
import datetime
import json


def utc_to_local(utc_dt):
    a = utc_dt.replace('T',' ')
    b = a.split(":00-")
    return b[0]

def run():
    f = "data/data.db"

    db = sqlite3.connect(f)
    c = db.cursor()
    
    q = "SELECT * from events"
    a = c.execute(q)


    jasons = []

    for item in c.fetchall():

        dic = {}

        dic["title"] = str(item[1])
        
        
        dic["details"] = str(item[2])
        dic["starts"] = int(time.mktime(datetime.datetime.strptime(utc_to_local(item[3]),"%Y-%m-%d %H:%M").timetuple()))*1000
        
        
        dic["ends"] = int(time.mktime(datetime.datetime.strptime(utc_to_local(item[4]),"%Y-%m-%d %H:%M").timetuple()))*1000
        
        cArray = item[5].split(",")

        
        dic["location"] = {}
        dic["location"]["coordinates"] = {}
        dic["location"]["coordinates"]["lat"] = float(cArray[0])
        dic["location"]["coordinates"]["lng"] = float(cArray[1])
        
        jasons.append(dic)

    return json.dumps(jasons)


#pass run() to endpoint
