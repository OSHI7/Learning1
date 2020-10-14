#%% IMPORTS
import matplotlib.pyplot as plt
import numpy as np
import addcopyfighandler

#%% FUNCTIONS
def SW_IL(maxIL=1, distribution='uniform', size=1):
    if distribution=='uniform':
        return np.random.uniform(0,maxIL,size=size)
    elif (distribution=='gaussian') or distribution=='normal':
        return np.random.normal(loc=maxIL / 2, scale=(maxIL / 2) / 3, size=size)
#%% SIM
Po=-10 # dB

maxIL=10
'''

''';

if 0: # Test distribution
    ILS =[]
    for i in range(0,1000):
        ILS.append(SW_IL(maxIL=maxIL,distribution='uniform'))

    plt.close('all')
    plt.plot(ILS)

# get first IL
IL0=SW_IL(maxIL=maxIL)[0]
IL0=7.
print(f'IL0={IL0}')
Pref = Po-IL0

# Get 100 next IL
N=1000
Pout = (Po-SW_IL(maxIL=maxIL, size=N))- Pref

Pout_mean = np.mean(Pout)
Pout[0] = 0
plt.close('all')
plt.plot(Pout)
plt.axhline(y=Pout_mean, color='r', linestyle='-')
plt.title(f'IL0={IL0:.2f}, avgIL={Pout_mean:.2f}')
# plt.title(f'IL0={IL0:.2f} $\overline{"IL0"}$ = {{{Pout_mean}}}')
plt.tight_layout()