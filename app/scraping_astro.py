import requests
import json
import os

sign = input("Please input your sign: ")

def zodiac_scrape(sign):
    #request_url = f"https://zodiacal.herokuapp.com/{sign}"
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/today/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    daily = parsed_response["horoscope"]
    print(daily)
    #request_url = f"http://horoscope-api.herokuapp.com/horoscope/week/{sign}"
    #response = requests.get(request_url)
    #parsed_response = json.loads(response.text)
    #week = parsed_response["horoscope"]
    #print(week)
    #request_url = f"http://horoscope-api.herokuapp.com/horoscope/month/{sign}"
    #response = requests.get(request_url)
    #parsed_response = json.loads(response.text)
    #month = parsed_response["horoscope"]
    #print(month)
    #request_url = f"http://horoscope-api.herokuapp.com/horoscope/year/{sign}"
    #response = requests.get(request_url)
    #parsed_response = json.loads(response.text)
    #year = parsed_response["horoscope"]
    #print(year)
#
zodiac_scrape(sign)