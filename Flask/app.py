from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os, sched, time
import atexit
from apscheduler.scheduler import Scheduler


from utils import parseDB, facebookEvents, sharedeventsFacebook

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')

cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(minutes=10)
def recurring():
    print "get"
    facebookEvents.getEvents()
    sharedEvents.get_shared_events()
    
@app.route("/") 
def hello_world():
    return render_template("index.html")
    

khal = [0,1,1,2,3,5,8]

@app.route("/showResults")
def test_tmplt():
    return render_template("result.html",table=parseDB.parse())

@app.route("/test_s")
def test_uts():
    return 'hi'

    
if __name__ == "__main__": 
    app.debug = True 
    app.run()
