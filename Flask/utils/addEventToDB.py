import sqlite3


def addEvent(title, desc, start, end, geo, add):

    f = "data/data.db"

    db = sqlite3.connect(f)
    c = db.cursor()

    q = "SELECT id from events"
    a = c.execute(q)


    id = 0
    
    for num in a:
        if num[0] > id:
            id = num[0]
    
    id += 1
    
    
    q = "INSERT INTO events VALUES ("
    q += "%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (id, title, desc, start, end, geo, add)
    c.execute(q)

    db.commit()
    db.close()
    




