from collections import Counter
from utils import utils


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
