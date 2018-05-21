from flask import Flask, request, render_template
import os
import datetime

app = Flask(__name__)


@app.route("/")
def show_hi():
    return render_template("index.html")

@app.route("/search")
def do_search():
    return "Search page"



@app.route("/photos/<id>")
def show_specific_photo(id):
    return "<h1>This is photo {0}</h1>".format(id)
    
@app.route("/cars/<fred>/image/<wilma>")
def show_car(fred, wilma):
    return "<h1>You asked for image {0} for car {1}</h1>".format(wilma, fred)
    

@app.route("/photos")
def show_photos():
    return "<h1>This is the photos page</h1>"

@app.route("/time")
def time():
    now = datetime.datetime.now()
    return "The current time is " + now.strftime("%H:%M:%S")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)