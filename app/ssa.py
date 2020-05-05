from bs4 import BeautifulSoup
import requests

def ssa_scrape(name, sex): 
    """
    Takes user inputted baby name and sex and insert into Social Security Admin website form to retrieve name popularity data.
    Params:
        Name (string); chosen first name of babay
        Sex (string); abbreivated Male as "M" or Female as "F"
    Examples:
        ssa_scrape("John", "M")
        ssa_scrape("Sarah", "F")
    """
    while True:
        request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
        params = {"name": name, "sex": sex}
        response = requests.post(request_url, params)
        soup = BeautifulSoup(response.text, "html.parser")
        if not "Please enter another name." in soup.text:
            facts = soup.body.find("ul").find("li")
            return facts.text
        else:
            return "Heg is not in the top 1000 names for any year of birth beginning with 2000. Please enter another name."

if __name__ == "__main__":

    sexes = ["M", "F"]

    name = input("Please enter your baby's first name: ")

    while True:
        sex = input("Please enter your baby's sex as either 'M' or 'F': ")    
        if sex in sexes:
            break      
        else: 
            print ("Hey, please enter your baby's  sex as either 'M' or 'F. Please try again!")

    ssa_scrape(name, sex)