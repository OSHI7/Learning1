import types
#import os
import inspect
import importlib
#importlib.reload(Utils)

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

#showModulePath(os)
