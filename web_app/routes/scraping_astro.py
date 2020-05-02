import requests

from flask import Blueprint, render_template, request

from app.scraping_astro import zodiac_scrape

astro_routes = Blueprint("astro_routes", __name__)

@scraping_astro.route("/zodiacresult")
def zodiac_scrape(sign):
    request_url = f"https://zodiacal.herokuapp.com/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return print(parsed_response)
