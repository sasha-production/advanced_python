from mod2.hello_world import app
import unittest
from freezegun import freeze_time

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("2024-03-11")
    def test_hello_world(self):
        name = 'Sasha'
        greet = 'Хорошего понедельника'
        response = self.app.get(self.base_url + name)
        response_text = response.data.decode()
        self.assertTrue(greet in response_text)

    @freeze_time("2024-03-11")
    def test_hello_world1(self):
        name = 'Sasha'
        greet = 'Хорошего вторника'
        response = self.app.get(self.base_url + name)
        response_text = response.data.decode()
        self.assertFalse(greet in response_text)
    @freeze_time("2024-03-13")
    def test_hello_world_name_as_day(self):
        name = 'Хорошей пятницы'
        greet = 'Хорошей среды'
        response = self.app.get(self.base_url + name)
        response_text = response.data.decode()
        self.assertTrue(greet in response_text)