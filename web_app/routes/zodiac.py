import requests

from flask import Blueprint, render_template, request

#from app.zodiac import zodiac_scrape

zodiac = Blueprint("zodiac", __name__)

#@zodiac.route("/result")
def zodiac_scrape(sign):
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/today/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    daily = parsed_response["horoscope"]
    print(zodiac_output)