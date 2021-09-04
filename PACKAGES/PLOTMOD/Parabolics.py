# -*- coding: utf-8 -*-
'''
j.philipson
10:35 PM, 2/25/2021
'''
import numpy as np
import matplotlib.pyplot as plt
import matlablib as mla

def parabola(x0=0, xmin=-1, xmax=+1, Npts=100):
    x=np.linspace(xmin, xmax, Npts)
    y=(x-x0)**2
    return x,y

def plotMe(x=None, y=None):
    fig,ax = plt.subplots(1,1)
    ax.plot(x,y,'-r.')
    ax.set_title('parabola')

if __name__ == '__main__':
    x,y=parabola(x0=0.2)
    plotMe(x,y)
