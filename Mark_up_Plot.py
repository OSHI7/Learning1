
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matlablib import *

plt.ion()
tic()
fname_1=r"70dB-2sec.csv"
fname_2=r'70dB-5sec.csv'
pd1=pd.read_csv(fname_1)
pd2=pd.read_csv(fname_2)
print('loaded')
toc()
y1 = pd1.RL1_1310
y2 = pd2.RL1_1310
x1 = np.linspace(1, len(y1), len(y1))
x2 = np.linspace(1, len(y2), len(y2))

# print(y1)

# Mean level of 2s
mean_2s = np.mean(y1)
mean_5s = np.mean(y2)

#%%

def makePlot():
    plt.figure()  # Make a new figure
    line_2s = plt.plot(x1, y1, label=("2s mean=" + str(round(mean_2s, 2))
                                      + ", std=" + str(round(np.std(y1), 2))))

    line_5s = plt.plot(x2, y2, label="5s mean=" + str(round(mean_5s, 2))
                                     + ", std=" + str(round(np.std(y2), 2)))
    plt.grid(1, which='major', axis='both')
    plt.title('2s vs 5s ATIME')
    # plt.legend(handles=[line_2s, line_5s])
    plt.legend()

    toc()
    plt.show(block=True)

##
#%% 
makePlot()

