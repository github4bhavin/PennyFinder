__author__ = 'bhavinpatel'

import AppConfig
import imaplib

class EmailParser:

    _outlook = None

    def __init__(self):

        self.__init_outlook()

    def __init_outlook(self):
        self._outlook = imaplib.IMAP4_SSL( AppConfig.outlook_server )
        self._outlook.login( AppConfig.outlook_login_name, AppConfig.outlook_login_password )
        self._outlook.select()

    def __get_all_messages(self):


