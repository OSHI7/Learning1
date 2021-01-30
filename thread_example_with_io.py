# -*- coding: utf-8 -*-
'''
j.philipson
9:32 PM, 1/27/2021
'''

import threading


#ref: https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python


def addMyNumbers(a,b):
    return a+b


x = threading.Thread(target=addMyNumbers, args=(1,2))
x.start()
x.join()
print(x)

print('done and sunny')
