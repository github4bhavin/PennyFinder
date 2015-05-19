
from lib.EmailParser import  EmailParser


from pprint import pprint

if __name__ == '__main__':
    ep = EmailParser()
    print ep.get_all_messages()