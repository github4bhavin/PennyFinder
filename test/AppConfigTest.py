__author__ = 'bhavinpatel'

import unittest
import lib.AppConfig

class AppConfigTest(unittest.TestCase):

    def test_outlook_server(self):
        self.assertIsNotNone( lib.AppConfig.outlook_server )

    def test_outlook_server_user(self):
        self.assertIsNotNone(lib.AppConfig.outlook_login_name)

    def test_outlook_server_pass(self):
        self.assertIsNotNone(lib.AppConfig.outlook_login_password)

if __name__ == '__main__':
    unittest.main()