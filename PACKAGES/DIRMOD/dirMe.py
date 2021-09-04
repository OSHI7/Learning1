# -*- coding: utf-8 -*-
'''
j.philipson
10:51 PM, 2/25/2021
'''


import os

def listDirectoryContents(mydir=None):
    if mydir is None:
        mydir = os.getcwd()
    else:
        pass
    contents = os.listdir(mydir) # returns list
    print(f"\ncontents of  >>{mydir}<< are:")
    for i, content in enumerate(contents):
        print(f"  item {i:}.  \t{content}")


if __name__ == '__main__':
    listDirectoryContents()