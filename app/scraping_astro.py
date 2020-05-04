import requests
import json

def zodiac_scrape(sign):
    """
    Takes user inputted astrological sign and compiles into request url.
    Params:
        Sign (string); one of 12 astrological signs determined by birthday
    
    Examples:
        zodiac_scrape(Gemini)
        zodiac_scrape(Taurus)
    """
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/today/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    daily = parsed_response["horoscope"]
    print(daily)
    exit()
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

sign = input("Please input your sign: ")
zodiac_scrape(sign)