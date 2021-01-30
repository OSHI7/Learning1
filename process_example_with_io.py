# -*- coding: utf-8 -*-
'''
j.philipson
10:59 PM, 1/27/2021
'''


import threading
import time
#

#
#
# return_value=[]
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     for i in range(0,100):
#         future = executor.submit(foo, 'world!')
#
#     for i in range(0,100):
#         return_value[i] = future.result()
#         print(return_value)
#
# print('done ya')

def threading_func(f):
    """Decorator for running a function in a thread and handling its return
    value or exception"""
    def start(*args, **kw):
        def run():
            try:
                th.ret = f(*args, **kw)
            except:
                th.exc = sys.exc_info()
        def get(timeout=None):
            th.join(timeout)
            if th.exc:
                # raise th.exc[0], th.exc[1], th.exc[2] # py2
                raise th.exc[1] #py3
            return th.ret
        th = threading.Thread(None, run)
        th.exc = None
        th.get = get
        th.start()
        return th
    return start

@threading_func
def foo(bar, val):
    print('hello {}'.format(bar))
    print('started!')
    time.sleep(val)
    print('done')
    return val

th=[]
for i in range(0,5):
    th.append( foo("text", i) )

try:
    for i in range(0,5):
        print(th[i].get())
except TypeError:
    print("exception thrown ok.")