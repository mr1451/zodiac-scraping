# Final_Project_OPIM244/routes/home_routes.py

from flask import Blueprint, render_template, redirect, flash, request 
import requests
from web_app.routes.ssa import ssa_scrape 
from web_app.routes.zodiac import zodiac_scrape
import os
import json

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

@home_routes.route("/result", methods=["GET"])
def pass_sign():
    sign = request.form["sign"]
    zodiac_output = zodiac_scrape(sign)
    return render_template("zodiacresult.html", sign = sign, zodiac_output = zodiac_output)

@home_routes.route("/result", methods=["POST"]) #https://www.youtube.com/watch?v=AEM8_4NBU04
def pass_ssa():
    name = request.form["name"]
    sex = request.form["sex"]
    output = ssa_scrape(name, sex)
    return render_template("result.html", ssa_output = ssa_output, name=name, sex=sex)
    