import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matlablib import *


## % load me file
# %timeit
# fname_1=r"D:\Works\Python\Learning1\70dB-2sec.csv"
# fname_2=r'D:\Works\Python\Learning1\70dB-5sec.csv'
tic()
fname_1=r"70dB-2sec.csv"
fname_2=r'70dB-5sec.csv'
pd1=pd.read_csv(fname_1)
pd2=pd.read_csv(fname_2)
print('loaded')
toc()

##
tic()
# only works for one plot - What if many are called?
# [plt.close(x) for x in range(1,11)]

closefigures(plt) # call my matplotlib to kill all open figures
# Nonense comment

##
# [ x**2 for x in range(1,11) ]

y1=pd1.RL1_1310
y2=pd2.RL1_1310
x1=np.linspace(1,len(y1), len(y1))
x2=np.linspace(1,len(y2), len(y2))

# print(y1)

# Mean level of 2s
mean_2s=np.mean(y1)
mean_5s=np.mean(y2)

plt.figure() # Make a new figure
line_2s=plt.plot(x1, y1, label=("2s mean="+ str(round(mean_2s, 2))
                                        + ", std=" +str(round(np.std(y1), 2))))

line_5s=plt.plot(x2,y2, label="5s mean=" + str(round(mean_5s,2))
                                        + ", std=" +str(round(np.std(y2), 2)))
plt.grid(1, which='major', axis='both')
plt.title('2s vs 5s ATIME')
#plt.legend(handles=[line_2s, line_5s])
plt.legend()

toc()

#plt.show()
plt.show(block = False)
##
if 1:
    print('hi dude')
    fix=plt.figure()
    plt.plot(x1, y1, label=("2s mean=" + str(round(mean_2s, 2))+ ", std=" + str(round(np.std(y1), 2))))
    #fix.show()
    plt.show(block=False)  # this is important to let code hit the breakpoints
    print('done')
    # ref: https://stackoverflow.com/questions/7449585/how-do-you-set-the-absolute-position-of-figure-windows-with-matplotlib

print('hi')
##
if 0:
    fig, ax = plt.subplots()
    mngr = plt.get_current_fig_manager()
    # to put it into the upper left corner for example:
    mngr.window.setGeometry(50, 100, 640, 545)

## Matlab style plotting?
fig=plt.figure();
plt.plot(x1,y1, '-r');
#fig.show(block=False)
fig.canvas.draw()
plt.pause(0.001)
# closefigures(plt)


##


