# Final_Project_OPIM244

## Setup

First, make sure to clone this repository to your own Github desktop. Once done, create a virtual enviroment with following code in the command line:

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

## Using BabyReader

After running the python script, copy  http://127.0.0.1:5000/ into your web browser and you will navigate to the BabyReader online app. Here, enter the desired information for the child you would like to learn more about: their name, sex, and in which time period their birthday falls. Click submit, and you will be redirected to a custom results page which will provide unique BabyReader insights on your child. If the child's name is not very popular, the results page may lack the relevant name information. To try again, or enter another set of information for a different person, simply click on the Home tab. Finally, to learn more about the app and its purpose, click on the About tab.