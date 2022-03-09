import requests

import validators as val

from bs4 import BeautifulSoup as bs


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
            except ConnectionError:
                return f"Website is not available."
            except requests.exceptions.ConnectionError:
                return "Connection Error. -> Invalid URL"
        return data

    def get_soup(self):
        website = self.fetch_data()
        if isinstance(website, requests.models.Response):
            return bs(website.text, 'html.parser').body.getText()
        return website
