''' I want to make some simple data to track the stats of uptime'''
from Utils import sendMail

#sendMail(["philipson00@gmail.com"], "subject", "text", ["D:\\User\\joshua\\My Pictures\\Samurai_with_sword.jpg"])

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 2, 100)
y=np.power(x,2)
plt.plot(x, y)
#plt.plot(x, np.power(x,0.5))

plt.title('TITLE')
plt.xlabel('X')
plt.ylabel('Y')

filename='D:\\works\\GitHub\\Learning1\\MYPLOT.png'
filename='D:\\Works\\Python\\Learning1\\MYPLOT.png'
plt.savefig(filename)
print('saved')

#sendMail(["philipson00@gmail.com"], "subject", "text", ["D:\\User\\joshua\\My Pictures\\Samurai_with_sword.jpg"])

smtpUser = '@gmail.com'
smtpPass = ''
plt.ion()

sendMail(["philipson00@gmail.com"], "subject", "text", [filename], smtpUser=smtpUser, smtpPass=smtpPass)
print('sent')

plt.show()


#TODO: put passwords into the file, that is not controlled in GitHub
