# Final_Project_OPIM244/routes/home_routes.py

from flask import Blueprint, render_template, redirect, flash, request 
import requests
from web_app.routes.scraping import ssa_scrape 
from web_app.routes.scraping_astro import zodiac_scrape

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html") 

@home_routes.route("/zodiacresult", methods =["POST"])
def zodiac():
    print("VISITED THE ZODIAC PAGE")
    #return "Zodiac (TODO)"
    return render_template("zodiacresult.html") 

@home_routes.route("/nameresult", methods=["POST"]) #https://www.youtube.com/watch?v=AEM8_4NBU04
def passvalue():
    name = request.form["name"]
    sex = request.form["sex"]
    #render_template("nameresult.html", name=name, sex=sex)
    output = ssa_scrape(name, sex)
    #output = response.text
    #print(name)
    #print (sex)
    return render_template("nameresult.html", output = output, name=name, sex=sex)
    