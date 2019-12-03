import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matlablib import *


## % load me file
# %timeit
# fname_1=r"D:\Works\Python\Learning1\70dB-2sec.csv"
# fname_2=r'D:\Works\Python\Learning1\70dB-5sec.csv'
fname_1=r"70dB-2sec.csv"
fname_2=r'70dB-5sec.csv'
pd1=pd.read_csv(fname_1)
pd2=pd.read_csv(fname_2)
print('loaded')


##
try:
    plt.close()
except:
    print('boogers')

y1=pd1.RL1_1310
y2=pd2.RL1_1310
x1=np.linspace(1,len(y1), len(y1))
x2=np.linspace(1,len(y2), len(y2))
# print(y1)

# Mean level of 2s
mean_2s=np.mean(y1)
mean_5s=np.mean(y2)

line_2s=plt.plot(x1, y1, label=("2s mean="+ str(round(mean_2s, 2))
                                        + ", std=" +str(round(np.std(y1), 2))))

line_5s=plt.plot(x2,y2, label="5s mean=" + str(round(mean_5s,2))
                                        + ", std=" +str(round(np.std(y2), 2)))
plt.grid(1, which='major', axis='both')
plt.title('2s vs 5s ATIME')
#plt.legend(handles=[line_2s, line_5s])
plt.legend()





plt.show()
##
if 1:
    print('hi dude')
    fix=plt.figure()
    plt.plot(x1, y1, label=("2s mean=" + str(round(mean_2s, 2))+ ", std=" + str(round(np.std(y1), 2))))
    fix.show()
    print('done')
    # ref: https://stackoverflow.com/questions/7449585/how-do-you-set-the-absolute-position-of-figure-windows-with-matplotlib

##
if 0:
    fig, ax = plt.subplots()
    mngr = plt.get_current_fig_manager()
    # to put it into the upper left corner for example:
    mngr.window.setGeometry(50, 100, 640, 545)