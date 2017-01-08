import sqlite3
import pytz

def utc_to_local(utc_dt):
    a = utc_dt.replace('T',' ')
    b = a.split(":00-")
    return b[0]
    

def parse():

    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    
    q = "SELECT * from events"
    a = c.execute(q)

    table = []

    sortTab = []

    for obj in a:
        sortTab.append(obj)
    
    sortTab.sort(key=lambda x: x[3], reverse=False)
    
    for entry in sortTab:
        title = entry[1]
        desc = entry[2]
        start = entry[3]
        end = entry[4]
        gps = entry[5].split(',')
        addr = entry[6];
       
        start =  utc_to_local(start)
        end = utc_to_local(end)
        
        en = []
        en.append(title)
        en.append(desc)
        en.append(start)
        en.append(end)
        en.append(gps)
        en.append(addr)
        table.append(en)


    return table


#print parse()
