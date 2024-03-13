from mod2.decrypt import decrypt
import unittest


class MyTest(unittest.TestCase):
    def test1(self):
        di = {'абра-кадабра.': 'абра-кадабра',
              '.': ''
              }
        for encrypted_line in di:
            decrypt_expected = di[encrypted_line]
            with self.subTest(encrypted_line=encrypted_line):
                self.assertEqual(decrypt_expected, decrypt(encrypted_line))

    def test2(self):
        """
        test for 2 and 3 dots in line
        """
        di = {'абраа..-кадабра': 'абра-кадабра',
              'абраа..-.кадабра': 'абра-кадабра',
              'абра--..кадабра': 'абра-кадабра',
              'абрау...-кадабра': 'абра-кадабра',
              '1..2.3': '23'}
        for encrypted_line in di:
            decrypt_expected = di[encrypted_line]
            with self.subTest(encrypted_line=encrypted_line):
                self.assertEqual(decrypt_expected, decrypt(encrypted_line))

    def test3(self):
        """
        tests for more than 3 dots in line
        """
        di = {'абра........': '',
              'абр......a.': 'a',
              '1.......................': ''}
        for encrypted_line in di:
            decrypt_expected = di[encrypted_line]
            with self.subTest(encrypted_line=encrypted_line):
                self.assertEqual(decrypt_expected, decrypt(encrypted_line))
