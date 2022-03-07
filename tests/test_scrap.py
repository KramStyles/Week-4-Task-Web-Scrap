import app

from unittest import main, TestCase
from utils.utils import common_words
from requests import get


class TestGetData(TestCase):
    def setUpClass(cls) -> None:
        url = 'https://pacesetterfrontier.com'
        result = get(url)

        cls.get_data = app.GetData(url)

    def test_validate_inputs(self):
        self.assertTrue(self.get_data.validate_inputs())
        self.assertRaises(self.get_data.validate_inputs(12), ValueError)
        self.assertEqual(self.get_data.validate_inputs('mark.eke@decagon.dev'), "Only valid web address allowed!")


    def test_for_soup_data(self):
        pass


class TestCleanData(TestCase):
    def setUp(self) -> None:
        pass

    def test_to_check_for_characters(self):
        pass

    def test_to_check_for_common_words(self):
        pass

    def test_to_check_for_most_used_words(self):
        pass


class TestPlotData(TestCase):
    def setUp(self) -> None:
        pass

    def test_for_data_plot(self):
        pass
