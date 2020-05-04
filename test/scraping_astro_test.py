import os
import pytest

from app.scraping_astro import zodiac_scrape

CI_ENV = os.environ.get("CI") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

@pytest.mark.skipif(CI_ENV==True, reason="to avoid configuring credentials on, and issuing requests from, the CI server")

#def test_zodiac_scrape():


#def test_ssa_scrape():