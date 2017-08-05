# To reload

#import importlib
#importlib.reload(Utils)

import types
#import os
import inspect
import importlib
import json
#importlib.reload(Utils)

Filename='uData.json'

def showModulePath(module):
        if (hasattr(module, '__name__') is False):
            print('Error: ' + str(module) + ' is not a module object.')
            return None
        moduleName = module.__name__
        modulePath = None
        if isinstance(moduleName, types.BuiltinFunctionType):
            modulePath = sys.modules[moduleName]
        else:
            modulePath = inspect.getsourcefile(module)
            modulePath = '<module \'' + moduleName + '\' from \'' + modulePath + 'c\'>'
        print(modulePath)
        return modulePath

def JSONEncode(obj):
    s=json.JSONEncoder().encode(obj)
    return s

def savePWFile(obj):
    s=JSONEncode(obj)
    with open(Filename, "w", newline="\r\n") as text_file:
        text_file.write(s)

def getPWFile():
    with open(Filename, 'r', newline="\r\n") as text_file:
        encodedJSONString=text_file.read()
    #Return dictionary with us and pw
    filedata=json.JSONDecoder().decode(encodedJSONString)
    return filedata

#showModulePath(os)
