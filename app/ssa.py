from bs4 import BeautifulSoup
import requests

sexes = ["M", "F"]

name = input("Please enter your baby's first name: ")

while True:
    sex = input("Please enter your baby's sex as either 'M' or 'F': ")    
    if sex in sexes:
        break      
    else: 
        print ("Hey, please enter your baby's sex as either 'M' or 'F. Please try again!")

def ssa_scrape(name, sex): #https://stackoverflow.com/questions/52835681/how-can-i-run-a-python-script-from-within-flask
    request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
    params = {"name": name, "sex": sex}
    response = requests.post(request_url, params)
    #print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    return print(soup)

ssa_scrape(name, sex)