import sqlite3


def addEvent(id, title, desc, start, end, geo, add):

    f = "data/data.db"

    db = sqlite3.connect(f)
    c = db.cursor()


    q = "SELECT id from events"
    a = c.execute(q)

    for num in a:
        if num == id:
            return False
    
    
    q = "INSERT INTO events VALUES ("
    q += "%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (id, title, desc, start, end, geo, add)
    c.execute(q)

    db.commit()
    db.close()
    
    return True



