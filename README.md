# Final_Project_OPIM244

## Setup

First, make sure to clone this repository to your own Github desktop. Once done, create a virtual enviroment with following code in the command line:

```sh
conda create -n ssa-data-env python=3.7 # (first time only)
conda activate ssa-data-env 
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file from within the repository: 

```sh
pip install -r requirements.txt
```

## Web App Usage

Run the app:

```py
FLASK_APP=web_app flask run
```