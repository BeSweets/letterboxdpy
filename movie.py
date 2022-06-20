import json
import re
import requests
from bs4 import BeautifulSoup
from json import JSONEncoder

class Movie:
    def __init__(self, title):
        self.title = title
        self.director = self.movie_director(title)

    def jsonify(self):
        return json.dumps(self, indent=4,cls=Encoder)

    def get_parsed_page(self, url):
        # This fixes a blocked by cloudflare error i've encountered
        headers = {
            "referer": "https://liquipedia.net/rocketleague/Portal:Statistics",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

    def movie_director(self, movie):
        movie = movie.replace(' ', '-')
        page = self.get_parsed_page("https://letterboxd.com/film/" + movie + "/")

        crew = page.find_all("span", text = 'Director')[0].parent.parent
        director = crew.findChildren("a")
        director = director[0].text

        return director

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
