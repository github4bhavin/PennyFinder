__author__ = 'bhavinpatel'

import re

class Test(object):

    def SubjectParser(self, subject ):

        symbolPattern = re.compile('(?P<symbol>new)')

        match = symbolPattern.search( subject )
        return  match.groupdict()['symbol'] if match is not None else match