__author__ = 'bhavinpatel'

import AppConfig
import imaplib
import email
import importlib
import glob
import os
import re

import logging

from pprint import pprint


logging.basicConfig( format = "%(asctime)15s %(levelname)7s %(message)s" , level= logging.DEBUG)

class EmailParser:

    _outlook  = None
    _plugins  = []
    _messages = []

    def __init__(self):

        self.__init_outlook()
        self._load_plugins()

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
            if i > 50:
                break
            for plugin in self._plugins:
                pluginClass = getattr( plugin , plugin.__name__.split('.')[-1])
                pluginClassObject = pluginClass()
                print ("\n (%s) sending subject : %s") % ( plugin.__name__, msg.get('Subject'))
                parsedSymbol = pluginClassObject.SubjectParser( msg.get('Subject'))
                print parsedSymbol


        return  '\n'.join( self._messages )

    def get_all_messages(self):
        return self.__get_all_messages()

    def _load_plugins(self):
        #m = importlib.import_module( 'lib.Plugins.Default');
        #c = getattr(m , 'Default')
        #o = c()
        #o.SubjectParser('test subject ABC')
        #print dir(m)
        #print type( m )

        allPluginFiles = glob.glob( os.path.dirname(__file__) + "/Plugins/*.py")
        for pluginFile in allPluginFiles:

            if pluginFile.find('__init__') >=0:
                continue


            pattern     = re.compile('\/lib\/Plugins\/(?P<PluginModuleName>\w+)')
            matchedName = pattern.search( pluginFile )
            if matchedName is not None:
                pluginName  = matchedName.groupdict()['PluginModuleName']
                self._plugins.append( importlib.import_module( "lib.Plugins." + pluginName ) )
                logging.info( "plugin loaded : %s " %( pluginName ) )
            else:
                logging.warning(  "Unable to load plugin from [%s]" %( pluginFile ) )


