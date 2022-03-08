import validators as val
import matplotlib.pyplot as plt

from requests import get
from bs4 import BeautifulSoup as bs
from collections import Counter

from utils import utils


class GetData:
    def __init__(self, url):
        self.url = url

    def validate_inputs(self, url='https://www.python.org'):
        return False

    def fetch_data(self):
        pass

    def get_soup(self):
        pass


class CleanData:
    def __init__(self, data):
        self.data = data

    def check_chars(self):
        pass

    def check_common_words(self):
        pass

    def generate_frequent_words(self, num_words=7):
        pass


class DisplayData:
    def __init__(self, words):
        self.words = words

    def convert_data(self):
        pass

    def plot_data(self):
        pass
