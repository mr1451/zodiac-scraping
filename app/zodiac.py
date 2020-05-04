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
    zodiac_output = parsed_response["horoscope"]
    return zodiac_output

def zodiac_scrape_week(sign):
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/week/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output_week = parsed_response["horoscope"]
    return zodiac_output_week

def zodiac_scrape_month(sign):
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/month/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output_month = parsed_response["horoscope"]
    return zodiac_output_month

def zodiac_scrape_year(sign):
    request_url = f"http://horoscope-api.herokuapp.com/horoscope/year/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output_year = parsed_response["horoscope"]
    return zodiac_output_year

if __name__ == "__main__":

    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Saggitarius", "Capricorn", "Aquarius", "Pisces"]

    while True:
        sign = input("Please enter your zodiac sign: ")    
        if sign in signs:
            break      
        else: 
            print ("Hey, there might be a mispelling in your sign. Please try again!")

    zodiac_scrape(sign)
    zodiac_scrape_week(sign)
    zodiac_scrape_month(sign)
    zodiac_scrape_year(sign)