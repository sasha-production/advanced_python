import unittest
from mod4.task1 import app

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = {'email': 'abc@ya.ru',
                     'phone': 1234567890,
                     'name': 'Sasha',
                     'address': 'Moscow',
                     'index': 1,
                     'comment': 'my_comment'}

    def test_email_checking_correct(self):
        expected_email = 'abc@ya.ru'
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.get_data(as_text=True)
        self.assertTrue(expected_email in response_text)

    def test_checking_email_empty(self):
        self.data['email'] = ''
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_checking_email_wrong(self):
        self.data['email'] = 'abcya.ru'
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_phone_checking_correct(self):
        expected_phone = '1234567890'
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.get_data(as_text=True)
        self.assertTrue(expected_phone in response_text)

    def test_phone_checking_wrong(self):
        self.data['phone'] = 999_999_999
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_name_checking_correct(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_name_checking_empty(self):
        self.data['name'] = ''
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_address_checking_correct(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_address_checking_empty(self):
        self.data['address'] = ''
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_index_correct(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_index_wrong(self):
        self.data['index'] = '1q'
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_index_empty(self):
        self.data['index'] = ''
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(400, response.status_code)

    def test_comment(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_comment_empty(self):
        self.data['comment'] = ''
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()