from bs4 import BeautifulSoup
import requests

def zodiac_scrape(sign):
    request_url = f"https://zodiacal.herokuapp.com/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return print(parsed_response)

# todo:
# soup = BeautifulSoup(response.text)