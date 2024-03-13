import unittest
from mod3.person import Person


class PersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Sasha', 2004, 'Ekaterinburg')

    def test_age(self):
        self.assertEqual(20, self.person.get_age())

    def test_name(self):
        self.assertNotEqual('Alexander', self.person.name)

    def test_set_name(self):
        self.person.set_name('Alexander')
        self.assertEqual('Alexander', self.person.name)

    def test_set_name1(self):
        self.person.set_name('Alexander')
        self.assertNotEqual('Sasha', self.person.name)

    def test_get_address(self):
        self.assertEqual('Ekaterinburg', self.person.address)

    def test_set_address(self):
        self.person.set_address('Moscow')
        self.assertEqual('Moscow', self.person.address)

    def test_homeless(self):
        self.assertEqual(False, self.person.is_homeless())