list=['happy', 'sad', 'quick', 'slow']


# for item in list:
#     print(item)
import numpy as np
import Utils

#%%  cell
list=['happy', 'sad', 'quick', 'slow']


for item in list:
    print(item)

i=iter(list)
#print(i())
print(i)
print('hello dead')

print('eh mon')

import matplotlib.pyplot as plt 


#%% Add and give back function
def addSubMultDivAndGiveBack(a,b):
    return(a+b, a-b, a*b, a/b, a, b)

print('hi') #ctrl+enter to jump to next line from within quotes


1 <= 2  3

[_ ,_ ,_ , _, e,f]=addSubMultDivAndGiveBack(8,2)

e,f=addSubMultDivAndGiveBack(90,10)[4:6]
*a,e,f=addSubMultDivAndGiveBack(90,10)

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
i=1;
if i  !=   2:
    print('eyman')

print("Graphical Representation : \n", np.square(x))

plt.title("blrreue : with square\nred : without square")
plt.plot(x, np.square(x))

plt.plot(x, x, color = 'red')
plt.show()
print(i)
print('all done, local change from Joshua-Pc')