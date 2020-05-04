from bs4 import BeautifulSoup
import requests

def ssa_scrape(name, sex): #https://stackoverflow.com/questions/52835681/how-can-i-run-a-python-script-from-within-flask
    request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
    params = {"name": name, "sex": sex}
    response = requests.post(request_url, params)
    #print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    return print(soup)
