#%%

# Causes pop-out graphics
import matplotlib
matplotlib.use('Qt5Agg') 

import matplotlib.pyplot as plt 

#plt.switch_backend('QtAgg4')

#get_ipython().run_line_magic('matplotlib', 'inline')
#%% 
figure,ax = plt.subplots()

ax.set_title('host')
ax.set_ylabel('hiffas')
ax.tight_layout()

# %%
