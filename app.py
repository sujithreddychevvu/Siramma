from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd
from datetime import date, time, datetime
import datetime
app = Flask(__name__)




@app.route('/')
def hello_world():
    today=date.today()
    date_time2 = datetime.date(2019, 5, 10)
    if(today>date_time2):
        print("hello")
    else:
        print("helliio")
    #return render_template("index.html")



   



if __name__ == '__main__':
    app.run(debug=True)
    

