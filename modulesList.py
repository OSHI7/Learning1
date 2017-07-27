# get a list of the system processes using pip freeze

import subprocess
import os.path
from io import open

if 1:

    Attempt1Succeed=1
    try:
        print('trying pip method 1..', end='')
        result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, universal_newlines=True)
        a=result.stdout
        #b=a.decode("utf-8")
        b=a
        print('..succeeded!')
    except:
        print('...failed ;(')
        Attempt1Succeed=0

    if not(Attempt1Succeed):
        try:
            print('trying py-m method 2..', end='')
            result=subprocess.run(['py' ,'-m', 'pip', 'freeze'], stdout=subprocess.PIPE, universal_newlines=True)
            a=result.stdout
            b=a
            print('..succeeded!')
        except:
            print('...failed!')
            #raise OSError(2, 'ProcessLookupError', 'py -m pip freeze')

#Get name of currently executing python file
FileName=(os.path.basename(__file__))
#print(type(FileName))

with open("ModulesList.txt", "w", newline="\r\n") as text_file:
    text_file.write('*'*63 + "\n")
    text_file.write("I MADE THIS LIST OF INSTALLED MODULES by running: %s \r" % FileName)
    text_file.write('*'*63 + "\n")
    text_file.write("%s" % b)

print('Done!')

