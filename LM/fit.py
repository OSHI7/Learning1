"""
Curve Fit example
@luis.fernandes
#Nov 20 2019
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def lorentzian(x, amplitude, x0, sigma, background):
    # A lorentzian peak with:
    #   Constant Background          : background
    #   Proportional to the maximum  : amplitude
    #   Central value                : x0
    #   Full Width at Half Maximum   : sigma
    #   Data                         : x
    return background+(amplitude/np.pi)/(1.0+((x-x0)/sigma)**2)

# Reference Acetylene peak
ref_ace_peak = 1521.06040 # R7 (Acetylene)

# Getting the data to fit
source_data = 'sample_data_to_fit.csv'
data = pd.read_csv(source_data, index_col=0)
x = data.index
y = data.P1

# Initial guesses for the fit parameters are very important,
# the better the guesses the better faster the fit converges.
# Bad initial guesses can lead to failed fitting attempts
############################################################################
background = y.mean()
x0 = ref_ace_peak
sigma = 0.002
amplitude = y.max()-background # Not the lorentzian max but close enough

# Running the curve fit algorithm:
# Arguments are the function to fit (lorentzian), the data (x, y),
# and the initial guesses (p0).
popt,pcov = curve_fit(lorentzian, x, y, p0=[amplitude, x0, sigma, background])

# popt and pcov are the outputs of the fit function.
# pcov has some details about convertion an other internals
# popt is an array that contains the resulting fitting parameters 
print(f'Fit results = {popt}')

# Calculating r_squared of the fit (optional)
residuals = y - lorentzian(x, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f'R**2 = {r_squared:.4f}', end='')

# Create a new array to plot the fit
xx = np.arange(x.min(), x.max(), 0.0001)

plt.plot(x, y,'o', label='Data')
plt.plot(xx, lorentzian(xx, *popt),'--', label='Fit')
plt.xlim([1521.00, 1521.12])
plt.legend()

plt.title('Line from gas cell')
plt.ylabel('IL (dB)')
plt.xlabel('Wavelength (nm)')
plt.savefig('sample_data_to_fit.png')
