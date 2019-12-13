import numpy as np
import timeit # ref
import matplotlib.pyplot as plt
from matlablib import *

closefigures(plt)


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


# x0=np.arange(1, 100,10, dtype=float)
N=1000;
x0=np.linspace(-10, 10, N)
x1=gaussian(x0, 0, .5)
x2=np.heaviside(x0,1, )




# x1=np.random.uniform(size=10000)
# x2=np.random.uniform(size=10000)
x3=np.convolve(x1,x2)

plt.plot(x1)
plt.plot(x2)
# plt.plot(x0,x3)
plt.show();

plt.figure()
plt.plot(x3)
plt.show();
# keyboard()