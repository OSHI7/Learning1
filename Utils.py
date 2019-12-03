# To reload

#import importlib
#importlib.reload(Utils)

import types
#import os
import inspect
import importlib
import json
#importlib.reload(Utils)

# GMAIL Stuff
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os
import datetime

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


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')





def sendMail(to, subject, text, files=[]):
    smtpUser = 'philipson00@gmail.com'
    smtpPass = 'musylmancosmopepper1221'

    assert type(to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = smtpUser
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                        % os.path.basename(file))
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(smtpUser,smtpPass)
    server.sendmail(smtpUser, to, msg.as_string())

    print('Done')

    server.quit()

