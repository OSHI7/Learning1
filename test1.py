list=['happy', 'sad', 'quick', 'slow']


# for item in list:
#     print(item)
import numpy as np

#%%  cell
list=['happy', 'sad', 'quick', 'slow']


for item in list:
    print(item)

i=iter(list)
#print(i())
print(i)

import matplotlib.pyplot as plt 

#%% cell2

x = np.array([2,3,1,0])
y=x^2

# Create an 1d array from a list
import numpy as np
list1 = [0,1,2,3,4]
arr1d = np.array(list1)

# Print the array and its type
print(type(arr1d))
arr1d

print("Graphical Representation : \n", np.square(x)) 
  
plt.title("blrreue : with square\nred : without square")
plt.plot(x, np.square(x)) 
  
plt.plot(x, x, color = 'red') 
plt.show()
print(i)
print('all done, local change from Joshua-Pc')