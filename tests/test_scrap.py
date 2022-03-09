import unittest
import app
import os

# import __mock__ as mock_site
import pandas as pd

from requests import get
from .__mock__ import *


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
        self.data = mock_site
        self.clean_data = app.CleanData(self.data, testing=True)

    def test_to_check_for_special_characters(self):
        self.assertIsNotNone(self.clean_data.remove_chars())
        self.assertIsInstance(self.clean_data.remove_chars(), list)

    def tearDown(self) -> None:
        del self.data
        del self.clean_data


class TestWords(unittest.TestCase):
    def setUp(self) -> None:
        self.clean_data = app.CleanData(mock_site, testing=True)

    def test_to_check_for_common_words(self):
        self.assertFalse('in' in self.clean_data.check_common_words())

    def test_to_check_for_most_used_words(self):
        self.assertEqual(len(self.clean_data.generate_frequent_words()), 10)

    def tearDown(self) -> None:
        del self.clean_data


class TestPlotData(unittest.TestCase):
    def setUp(self) -> None:
        self.display_data = app.DisplayData(mock_frequent_words)

    def test_to_convert_data(self):
        self.assertIsInstance(self.display_data.convert_data(), pd.core.frame.DataFrame)

    def tearDown(self) -> None:
        del self.display_data


class TestLog(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.exists(os.getcwd())
        self.bad_path = os.path.exists(os.getcwd() + '/source')

    def test_for_logs(self):
        self.assertTrue(self.path)
        self.assertFalse(self.bad_path)


if __name__ == '__main__':
    unittest.main()
