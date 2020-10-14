import collections
import sys
import time

DataPoint=collections.namedtuple("DataPoint", "id, x, y, helven")


# DataPoint(d_id, x, y, temp, quality)

p1=DataPoint(1, 10,11, None)
p2=DataPoint(2, 10,12, 'apple')


for i in range(10):
    print(i, end='')
    time.sleep(0.1)
    sys.stdout.flush

print(' done!')

#%%
mydict=dict(zip(['field1', 'field-two', 'field3'], [1, 2, 3]))

for k,v in mydict.items():
    print(f'Key={k}, Value={v}')


#%%

items = ['a' , 'b', 'C', "Dee"]
for i, item in enumerate(items):
    print(f'index = {i}' , end  = '  ')
    print(f'             item = {item}')



#%%
a=[]
a=[i for i,j in enumerate(items)]
print(a)
# Above prints [0,1,2,3], just the enumerated items

a=[]
a=[i for i in enumerate(items)]
print(a) # prints the entire dictionary

a=[]
a=[k for i,j in enumerate(items)]
print(a) # prints the entire dictionary

