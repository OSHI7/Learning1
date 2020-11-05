def HeyJosh(comment, comment2):
    print("Hey Josh ", comment,  "comment 2=", comment2)
    return (comment, comment2)



HeyJosh('hi', 'dude')


def foo (a):
    x=a
    y=a*2
    return (x,y)

(x,y) = foo(50)




def HeyJosh (comment,comment2):
    print('Hey Josh', comment, 'comment2=', comment2)
    return (comment,comment2)

HeyJosh('comment1', 'comment2')


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

