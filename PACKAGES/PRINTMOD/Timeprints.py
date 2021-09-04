# -*- coding: utf-8 -*-
'''
j.philipson
10:41 PM, 2/25/2021
'''

from datetime import datetime

def HowSoonIsNow():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    HowSoonIsNow()
    print('done')
