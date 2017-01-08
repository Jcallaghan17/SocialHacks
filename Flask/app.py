from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os

from utils import parseDB#, facebookEvents

app = Flask(__name__)


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
