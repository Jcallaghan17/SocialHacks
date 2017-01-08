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


    dics = []

    for item in c.fetchall():
        dic = {}
        dic["title"] = item[1]
        dic["details"] = item[2]
        dic["starts"] = int(time.mktime(datetime.datetime.strptime(utc_to_local(item[3]),"%Y-%m-%d %H:%M").timetuple()))
        
        
        dic["ends"] = int(time.mktime(datetime.datetime.strptime(utc_to_local(item[4]),"%Y-%m-%d %H:%M").timetuple()))
        
        cArray = item[5].split(",")

        
        dic["location"] = {}
        dic["location"]["coordinates"] = {}
        dic["location"]["coordinates"]["lat"] = float(cArray[0])
        dic["location"]["coordinates"]["lng"] = float(cArray[1])
        dics.append(dic)

    return dics


print run()
