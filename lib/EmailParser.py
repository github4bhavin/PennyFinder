__author__ = 'bhavinpatel'

import AppConfig
import imaplib
import email

from pprint import pprint

class EmailParser:

    _outlook = None
    _messages = []

    def __init__(self):

        self.__init_outlook()

    def __init_outlook(self):
        self._outlook = imaplib.IMAP4_SSL( AppConfig.outlook_server )
        self._outlook.login( AppConfig.outlook_login_name, AppConfig.outlook_login_password )
        self._outlook.select()

    def __get_all_messages(self):
        if self._outlook is None:
            raise "unable to connect to outlook"

        type, data = self._outlook.search( None , 'ALL')
        i = 0
        for messageNo in data[0].split():
            mtype , mdata = self._outlook.fetch( messageNo , 'RFC822')
            msg = email.message_from_string( mdata[0][1] )
            _col = []
            _col.append( msg.get('Date') )
            _col.append( msg.get('From') )
            _col.append( msg.get('Subject') )

            self._messages.append( ','.join( _col ))
            i += 1
            if i > 10:
                break

        return  '\n'.join( self._messages )

    def get_all_messages(self):
        return self.__get_all_messages()

