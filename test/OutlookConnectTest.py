__author__ = 'bhavinpatel'

import unittest
import imaplib
import lib.AppConfig

class OutlookConnectTest( unittest.TestCase):

    def setUp(self):
        self.outlook = imaplib.IMAP4_SSL( lib.AppConfig.outlook_server )

    def test_connect_outlook(self):
        self.outlook.login(  lib.AppConfig.outlook_login_name
                            ,lib.AppConfig.outlook_login_password )

if __name__ == '__main__':
    unittest.main()
