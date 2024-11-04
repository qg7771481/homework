import time
import random
from dataclasses import dataclass
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, abort
from flask.json import dumps
from time import time
app = Flask(__name__) #main

list1 = ["Вчора", "пооосле завтра"]
list2 = ["на вас", "ви", "на вас"]
list3 = ["упаде андроеднийколайдер", "побачете як риба буде танцювать гопака на пальмі", "повинні поставити все імущество на красний"]

# @app.route("/home/")


@app.get("/")
def home_world():
    return render_template('index.2.html')






@app.get('/menu')
def menu():
    pizzas = [
        {"name": "Маргарита", "ingredients": "риба, сир с плесеню", "price": 1500},
        {"name": "Пепероні", "ingredients": "тісто, тісто, пепероні", "price": 18},
        {"name": "Гавайська", "ingredients": " соус, моцарела, шинка, ананас", "price": 0}
    ]
    order = request.args.get('order', 'asc')
    return render_template('index.html', order=order, pizzas=pizzas)
@app.get("/home/")
def hello_world():
    return render_template("index3.html", title="ПіццаУпаняно")


# @app.route("/")


@app.get("/login/")
def get_login():
    return render_template("login.html")



@app.post("/login/")
def post_login():
    user = request.form["name"]
    info = request.user_agent
    if user == "aboba":
        abort(401)
    if user == "admin":
        return f"Are you is {user}from {info}"
    else:
        return redirect(url_for("get_login"), code=302)


@app.get("/info/")
def info():
    return (f"URL:\n{url_for("index")}\n"
            f"{url_for("choice")}\n"
            f"{url_for("get_login")}\n"
            f"{url_for("info")}\n")

@app.errorhandler(404)
def page_not_found(error):
    return ""


max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "score": 100},
  {"name": "Sviatoslav", "score": 99},
  {"name": "Юстин", "score": 100},
  {"name": "Viktor", "score": 79},
  {"name": "Ярослав", "score": 93},
]

@app.get('/results')
def results():
  context={
     "title": "Results",
     "students": students,
     "test_name": test_name,
     "max_score": max_score,

  }
  return render_template("results2.html", **context)


# @app.get @app.post @app.delete @app.put


if __name__ == "__main__":
    app.run(port=8010, debug=True)

#extends
#include