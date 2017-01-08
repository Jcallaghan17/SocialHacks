import sqlite3
from geopy.geocoders import GoogleV3, Nominatim

#AIzaSyCfq1QRfIb3OxIvLMwcbKymZ1E0AbaLIds

def addEvent(ide, title, desc, start, end, geo, add):

    ide = int(ide)
    
    f = "data/data.db"

    db = sqlite3.connect(f)
    c = db.cursor()


    q = "SELECT id from events"
    a = c.execute(q)

    #print "IDDDDDDDDDDDD: " + str(ide)
    
    for num in a:
        #print "IIIIIIIDDDDDDEEEEEEEE: " + str(num[0])
        if num[0] == ide:
            return False

        
    geolocator = Nominatim()
    location = geolocator.geocode(add)
    getGeo = "%f,%f" % (location.latitude,location.longitude) 

    
    q = "INSERT INTO events VALUES ("
    q += "%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (ide, title, desc, start, end, getGeo, add)
    c.execute(q)

    db.commit()
    db.close()
    
    return True



