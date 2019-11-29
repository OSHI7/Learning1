list=['happy', 'sad', 'quick', 'slow']


# for item in list:
#     print(item)
import numpy as np

list=['happy', 'sad', 'quick', 'slow']


for item in list:
    print(item)

i=iter(list)
#print(i())
print(i)

import matplotlib.pyplot as plt 



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

pos2 = []
def onclick(event):
    pos2.append([event.xdata,event.ydata])

plt.show()
print(i)
print('all done, local change from Joshua-Pc')


import matplotlib.pylab as plt
import numpy as np

f,a = plt.subplots()
x = np.linspace(1,10,100)
y = np.sin(x)
a.plot(x,y)

pos = []
def onclick(event):
    pos.append([event.xdata,event.ydata])

f.canvas.mpl_connect('button_press_event', onclick)
f.show()