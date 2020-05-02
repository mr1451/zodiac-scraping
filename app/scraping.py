#import requests
#from bs4 import BeautifulSoup
#
#url = 'https://www.ssa.gov/cgi-bin/babyname.cgi'
#post_params = {'value': 'Alex', 'value': 'M'}
#response = requests.post(url, data=post_params)
#soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

import requests
#import cgi


#form = cgi.FieldStorage()
#
#name =  form.getvalue('name')
#sex = form.getvalue('sex')


name = input("Please enter your baby's first name: ")
sex = input("Please enter your baby's sex as either 'M' or 'F': ")

def ssa_scrape(name, sex):
    request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
    params = {"name": name, "sex": sex}
    response = requests.post(request_url, params)
    print(response.status_code)
    return print(response.text)

ssa_scrape(name, sex)

#breakpoint()
# todo:
# soup = BeautifulSoup(response.text)