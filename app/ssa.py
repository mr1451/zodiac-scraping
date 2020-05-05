from bs4 import BeautifulSoup
import requests

def ssa_scrape(name, sex): 
    request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
    params = {"name": name, "sex": sex}
    response = requests.post(request_url, params)
    soup = BeautifulSoup(response.text, "html.parser")
    facts = soup.body.find("ul")
    return facts.text

if __name__ == "__main__":

    sexes = ["M", "F"]

    name = input("Please enter your baby's first name: ")

    while True:
        sex = input("Please enter your baby's sex as either 'M' or 'F': ")    
        if sex in sexes:
            break      
        else: 
            print ("Hey, please enter your baby's sex as either 'M' or 'F. Please try again!")

    ssa_scrape(name, sex)