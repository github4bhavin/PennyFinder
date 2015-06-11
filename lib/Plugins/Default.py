__author__ = 'bhavinpatel'

import re

class Default(object):

    def SubjectParser(self, subject ):

        symbolPattern = re.compile('[A-Z]{3,5}')
        symbolPattern.match( subject )