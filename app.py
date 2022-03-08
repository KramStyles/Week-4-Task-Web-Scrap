import requests

import validators as val
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup as bs
from collections import Counter

from utils import utils


class GetData:
    def __init__(self, url):
        self.url = url

    def validate_inputs(self, url='https://www.python.org'):
        if url and url != 'https://www.python.org':
            self.url = url
        if not self.url:
            return False
        elif type(self.url) != str or self.url.isdigit():
            return ValueError('Only string inputs are allowed')
        elif isinstance(val.url(self.url), val.utils.ValidationFailure):
            return 'Only valid web address allowed!'
        return True

    def fetch_data(self):
        data = self.validate_inputs()
        if data == True:
            try:
                return requests.get(self.url)
            except ConnectionError as err:
                return f"Website is not available."
            except requests.exceptions.ConnectionError as err:
                return "Connection Error. -> Invalid URL"
        return data

    def get_soup(self):
        website = self.fetch_data()
        if isinstance(website, requests.models.Response):
            return bs(website.text, 'html.parser').body.getText()
        return website


class CleanData:
    def __init__(self, data):
        self.data = data
        self.words = self.generate_frequent_words()

    def remove_chars(self):
        return self.data.split()

    def check_common_words(self):
        result = self.remove_chars()
        all_text = [word.lower() for word in result if word.isalpha() and word not in utils.common_words]
        return all_text

    def generate_frequent_words(self):
        self.data = Counter(self.check_common_words()).most_common(10)
        return self.data


class DisplayData:
    def __init__(self, words):
        self.words = words
        self.convert_data()
        self.plot_data()

    def convert_data(self):
        self.words = pd.DataFrame(self.words)
        return self.words

    def plot_data(self):
        axis_x = self.words[0]
        axis_y = self.words[1]
        plt.bar(axis_x, axis_y)
        plt.show()

        plt.pie(axis_y, labels=axis_x, shadow=True, explode=np.random.uniform(low=0.05, high=0.05, size=axis_x.size))
        plt.pie(axis_y, labels=axis_x, shadow=True)
        plt.show()


class Run:
    def __init__(self):
        run = input('Would you like to scrape a website (y/n)? ')
        while run.lower() != 'n':
            url = input('Enter a website to analyze!: ')
            self.data = GetData(url)
            self.soup = self.data.get_soup()
            if type(self.soup) == str and len(self.soup) > 50:
                self.cleaned_data = CleanData(self.soup)
                print('The top word is:', self.cleaned_data.words[0][0])
                self.plot_data = DisplayData(self.cleaned_data.words)
            else:
                print(self.soup)

            run = input('Would you like to scrape a website (y/n)? ')
        print('Thanks for analyzing! Come back again!')


if __name__ == '__main__':
    Run()
