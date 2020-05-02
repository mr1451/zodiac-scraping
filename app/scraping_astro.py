import requests

sign = input("Please input your sign.")

def zodiac_scrape(sign):
    request_url = f"https://zodiacal.herokuapp.com/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return print(parsed_response)
