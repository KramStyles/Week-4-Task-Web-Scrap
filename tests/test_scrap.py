import app

from unittest import main, TestCase
from utils.utils import common_words
from requests import get


class TestGetData(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'https://pacesetterfrontier.com'
        cls.result = get(cls.url)
        cls.get_data = app.GetData(cls.url)

    def test_validate_inputs(self):
        self.assertTrue(self.get_data.validate_inputs())
        self.assertRaises(self.get_data.validate_inputs(12), ValueError)
        self.assertEqual(self.get_data.validate_inputs('mark.eke@decagon.dev'), "Only valid web address allowed!")

    def test_for_fetching_data(self):
        self.assertTrue(self.result.ok)
        self.assertEqual(self.result.status_code, 200)
        self.url = 'https://solu.com'
        self.assertRaises(self.get_data.fetch_data(), ConnectionError)

    def test_for_soup_data(self):
        self.assertIsInstance(self.get_data.get_soup(), app.bs)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.url
        del cls.result
        del cls.get_data


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


if __name__ == '__main__':
    main()