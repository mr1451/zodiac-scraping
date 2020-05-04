import requests

from flask import Blueprint, render_template, request

#from app.scraping_astro import zodiac_scrape

#scraping_astro = Blueprint("scraping_astro", __name__)

@zodiacresult_astro.route("/zodiacresult")
def zodiac_scrape(sign):
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/today/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    daily = parsed_response["horoscope"]
    print(daily)
    return render_template("zodiacresult.html", daily = daily)