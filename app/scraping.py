import requests

name = input("Please enter your baby's first name: ")
sex = input("Please enter your baby's sex as either 'M' or 'F': ")

def ssa_scrape(name, sex):
    request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
    params = {"name": name, "sex": sex}
    response = requests.post(request_url, params)
    print(response.status_code)
    return print(response.text)

ssa_scrape(name, sex)