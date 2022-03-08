import requests

import validators as val
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup as bs
from collections import Counter

from utils import utils


class GetData:
    def __init__(self, url):
        self.url = url

    def validate_inputs(self, url='https://www.python.org'):
        if not url:
            return False
        elif type(url) != str:
            return ValueError('Only string inputs are allowed')
        elif not val.url(url):
            return 'Only valid web address allowed!'
        return True

    def fetch_data(self):
        if self.validate_inputs() == True:
            try:
                return requests.get(self.url)
            except ConnectionError as err:
                return f"{self.url} is not available. -≥ {err}"

    def get_soup(self):
        website = self.fetch_data()
        if isinstance(website, requests.models.Response):
            return bs(website.text, 'html.parser').body.getText()


class CleanData:
    def __init__(self, data):
        self.data = data

    def remove_chars(self):
        return self.data.split()

    def check_common_words(self):
        result = self.remove_chars()
        all_text = [word.lower() for word in result if word.isalpha() and word not in utils.common_words]
        return all_text

    def generate_frequent_words(self):
        return Counter(self.check_common_words()).most_common(10)


class DisplayData:
    def __init__(self, words):
        self.words = words

    def convert_data(self):
        pass

    def plot_data(self):
        pass
