import unittest
import app

import __mock__ as mock
import pandas as pd
import matplotlib.pyplot as plt

# from unittest import main, TestCase
from utils.utils import common_words
from requests import get


class TestGetData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'https://pacesetterfrontier.com'
        cls.result = get(cls.url)
        cls.get_data = app.GetData(cls.url)

    def test_validate_inputs(self):
        self.assertTrue(self.get_data.validate_inputs())
        self.assertIsInstance(self.get_data.validate_inputs(12), ValueError)
        self.assertEqual(self.get_data.validate_inputs('mark.eke@decagon.dev'), 'Only valid web address allowed!')

    def test_for_fetching_data(self):
        self.assertTrue(self.result.ok)
        self.assertEqual(self.result.status_code, 200)

    def test_for_soup_data(self):
        self.assertIsInstance(self.get_data.get_soup(), str)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.url
        del cls.result
        del cls.get_data


class TestCleanData(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_site = mock.mock_site
        self.clean_data = app.CleanData(self.mock_site)

    def test_to_check_for_special_characters(self):
        self.assertIsNotNone(self.clean_data.remove_chars())
        self.assertIsInstance(self.clean_data.remove_chars(), list)


class TestWords(unittest.TestCase):
    def setUp(self) -> None:
        self.clean_data = app.CleanData(mock.mock_site)
        self.mock_site = self.clean_data.remove_chars()

    def test_to_check_for_common_words(self):
        self.assertFalse('in' in self.clean_data.check_common_words())

    def test_to_check_for_most_used_words(self):
        self.assertEqual(len(self.clean_data.generate_frequent_words()), 10)

    def tearDown(self) -> None:
        del self.clean_data
        del self.mock_site


class TestPlotData(unittest.TestCase):
    def setUp(self) -> None:
        self.display_data = app.DisplayData(mock.mock_frequent_words)

    def test_to_convert_data(self):
        self.assertIsInstance(self.display_data.convert_data(), pd.core.frame.DataFrame)

    def test_for_logs(self):
        pass


if __name__ == '__main__':
    unittest.main()
