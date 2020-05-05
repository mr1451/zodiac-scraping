import os
import pytest

from app.zodiac import zodiac_scrape, zodiac_scrape_week, zodiac_scrape_month, zodiac_scrape_year

CI_ENV = os.environ.get("CI") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

@pytest.mark.skipif(CI_ENV==True, reason="to avoid configuring credentials on, and issuing requests from, the CI server")

def test_math():
    assert 5 == 5

def test_zodiac_scrape():
    sign = "Gemini"

    parsed_response = zodiac_scrape(sign)

    assert isinstance(parsed_response, str)

def test_zodiac_scrape_week():
    sign = "Gemini"

    parsed_response = zodiac_scrape_week(sign)

    assert isinstance(parsed_response, str)

def test_zodiac_scrape_month():
    sign = "Gemini"

    parsed_response = zodiac_scrape_month(sign)

    assert isinstance(parsed_response, str)

def test_zodiac_scrape_year():
    sign = "Gemini"

    parsed_response = zodiac_scrape_year(sign)

    assert isinstance(parsed_response, str)