## BabyReader

## Setup

First, make sure to clone this repository [https://github.com/mr1451/zodiac-scraping] to your own Github desktop. Once done, create a virtual enviroment with following code in the command line:

```sh
conda create -n ssa-zodiac-env python=3.7 # (first time only)
conda activate ssa-zodiac-env 
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file from within the repository: 

```sh
pip install -r requirements.txt
```

## Tests

Install pytest package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest --disable-pytest-warnings
```

## Web App Usage

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```py
FLASK_APP=web_app flask run
```

### Web App Functionality

BabyReader scrapes data from a horoscope API, http://horoscope-api.herokuapp.com/, using the sign input, and https://www.ssa.gov/cgi-bin/babyname.cgi using the name and sex inputs. In order to make these web requests, the requests package is included in requirements.txt. The BeautifulSoup package is also needed, to parse the name website's HTML contents.

The flask package, also included in the requirements.txt file,must be installed in order to run the flask app using the web server on the user's local machine. The dotenv package allows the program to reference variables from the .env file, which has been hidden from version control.

The web_app/templates folder includes 3 jinja templates along with a boostrap layout template, to generate and display the app's web pages.

## Code Quality

This repo is configured with Travis CI and integrated with Code Climate, for quality control measures. Thus, the repo includes  .travis.yml to further configure the CI server.

## Using BabyReader

After running the python script, copy  http://127.0.0.1:5000/ into your web browser and you will navigate to the BabyReader online app. Here, enter the desired information for the child you would like to learn more about: their name, sex, and in which time period their birthday falls. Click submit, and you will be redirected to a custom results page which will provide unique BabyReader insights on your child. If the child's name is not very popular, the results page may lack the relevant name information. To try again, or enter another set of information for a different person, simply click on the Home tab. Finally, to learn more about the app and its purpose, click on the About tab.