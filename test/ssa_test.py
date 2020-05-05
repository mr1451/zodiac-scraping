from bs4 import BeautifulSoup
import pytest
import requests
from app.ssa import ssa_scrape

@pytest.fixture()

def ssa():
    return requests.get("https://www.ssa.gov/cgi-bin/babyname.cgi")

class TestSSA:
    def test_alive(self, ssa):
        assert ssa.status_code == 200
    def test_html_title(self, ssa):
        soup = BeautifulSoup(ssa.content, "html.parser")
        assert "Popular Baby Names" in soup.text