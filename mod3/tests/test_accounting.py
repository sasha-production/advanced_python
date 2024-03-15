from mod2.accounting import app, storage
import unittest


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        di = {2024: {1: {1: 0}, 3: {13: 0, 12: 100_000, 11: 50_000}}}
        storage.update(di)

    def test_add1(self):
        url = "add/20240101/0"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertIn('0', response_data)

    def test_add2(self):
        url = "add/20240312/50000"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertIn('150000', response_data)

    def test_add3(self):
        url = "add/20240101/100"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertIn('100', response_data)

    def test_add_wrong_date(self):
        url = "add/_20240401/100"
        with self.assertRaises(ValueError):
            self.app.get(url)

    def test_calculate_month1(self):
        url = "/calculate/2024/09"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertEqual('0', response_data)

    def test_calculate_month2(self):
        url = "/calculate/2024/03"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertIn('200000 p.', response_data)

    def test_calculate_month3(self):
        url = "/calculate/2024/01"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertIn('100 p.', response_data)
    def test_calculate_year1(self):
        url = "/calculate/2024"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertIn('200100', response_data)

    def test_calculate_year2(self):
        url = "/calculate/2023"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertEqual('0', response_data)

    def test_calculate_year3(self):
        storage.clear()
        url = "/calculate/2024"
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertEqual('0', response_data)