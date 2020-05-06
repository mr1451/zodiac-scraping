#test/zodiac_test.py

import os
import pytest
import requests
import json

from app.zodiac import zodiac_scrape, zodiac_scrape_week, zodiac_scrape_month, zodiac_scrape_year

CI_ENV = os.environ.get("CI") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

@pytest.mark.skipif(CI_ENV==True, reason="to avoid configuring credentials on, and issuing requests from, the CI server")

def test_zodiac_scrape():
    sign = "Gemini"

    request_url = f"http://horoscope-api.herokuapp.com/horoscope/today/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output = zodiac_scrape(sign)

    assert parsed_response["sunsign"] == sign
    assert "horoscope" in parsed_response
    assert "sunsign" in parsed_response
    assert isinstance(zodiac_output, str)
    
def test_zodiac_scrape_week():
    sign = "Gemini"

    request_url = f"http://horoscope-api.herokuapp.com/horoscope/week/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output_week = zodiac_scrape_week(sign)

    assert parsed_response["sunsign"] == sign
    assert "horoscope" in parsed_response
    assert "sunsign" in parsed_response
    assert isinstance(zodiac_output_week, str)

def test_zodiac_scrape_month():
    sign = "Gemini"

    request_url = f"http://horoscope-api.herokuapp.com/horoscope/month/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output_month = zodiac_scrape_month(sign)

    assert parsed_response["sunsign"] == sign
    assert "horoscope" in parsed_response
    assert "sunsign" in parsed_response
    assert isinstance(zodiac_output_month, str)

def test_zodiac_scrape_year():
    sign = "Gemini"

    request_url = f"http://horoscope-api.herokuapp.com/horoscope/year/{sign}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    zodiac_output_year = zodiac_scrape_year(sign)

    assert parsed_response["sunsign"] == sign
    assert "horoscope" in parsed_response
    assert "sunsign" in parsed_response
    assert isinstance(zodiac_output_year, str)