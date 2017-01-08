from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os, sched, time
import atexit
from apscheduler.scheduler import Scheduler


from utils import parseDB, facebookEvents, sharedeventsFacebook, ical_parser

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')

cron = Scheduler(daemon=True)
cron.start()

def syncFacebookEvents():
    with app.app_context():
        facebookEvents.getEvents()
        print "got fb events"

def syncSharedEvents():
    with app.app_context():
        sharedeventsFacebook.get_shared_events()
        print "got fb shared events"

"""
def syncICalEvents():
    with app.app_context():
        ical_parser.sync_events()
        print "got ical events"
"""

@app.before_first_request
def initialize():
    apsched = Scheduler()
    apsched.start()

    apsched.add_interval_job(syncFacebookEvents, seconds=10)
    print "added job 1"
    apsched.add_interval_job(syncSharedEvents, seconds=10)
    print "added job 2"
    # apsched.add_interval_job(syncICalEvents, seconds=10)
    # print "added job 3"

"""
@cron.interval_schedule(seconds=20)
def recurring():
    print "getting update"
    #facebookEvents.getEvents()
    print "\tgot facebook events"
    #sharedEvents.get_shared_events()
    print "\tgot facebook shared events"
    icalparser.sync_events()
    print "\tpulled ical"
"""

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
