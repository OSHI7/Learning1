# EDITOR > File and Code Templates put this here!

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-10,10,100)
y=x**2

#%%
plt.close('all')
plt.ion()
plt.style.use('seaborn')  # style sheet reference: https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
fig, ax = plt.subplots( 1,1)#, figsize=(12,9), sharex=False)  #W x H
#fig = matplotlib.pyplot.figure

plt.plot(x,y, color='orange', linestyle='-')

# Do this, then get autocomplete pop-ups on plt
assert isinstance(ax, matplotlib.axes._subplots.Subplot)

# ax.

#%%
