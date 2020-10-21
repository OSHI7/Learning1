'''
Josh P.
Oct 20, 2020
Sample code for showing how to store NUMPY array in a single cell in a dataframe
    Data stored in dataframe
    Data extracted from dataframe
    Data stored to file
    Data read from file
'''

#%% Imports
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

#%% bonus: Demo for 3 ways how to build an array in a loop

# Use built-in
array=[]
for i in range(0,10):
    array.append(i)
# print(array)

# Assign/append next element using "+="
array=[]
for i in range(0,10):
    array+=[i]
# print(array)

# List compreshension
array = [i for i in range(0,10)];
# print(array)

#%% CALCULATION,

pd.set_option('display.max_columns', None)  # let pandas print out all the columns
column_names = ['Timestamp', 'Test_index', 'OTDRX', 'OTDRY']
df = pd.DataFrame(columns=column_names)

n_trials = 3
plt.ion()
plt.close('all')
fig, ax = plt.subplots( 1,1, figsize=(12,9), sharex=False)  #W x H

dict1 = {}
Test_index = 0
rows_list =[]
for i in range(0,n_trials):
    Timestamp = pd.Timestamp.now()
    Test_index += 1
    x = np.linspace(0,10,5)
    exponent = i+1 #np.random.uniform(low=0.001, high=0.5)
    print(f'exponent is: {exponent:.4f}')
    y= x**exponent
    plt.plot(x,y, marker = '^')
    dict1 = {'Timestamp':Timestamp,
             'Test_index':Test_index,
             'OTDRX': x,
             'OTDRY': y
             }
    rows_list.append(dict1)
ax.set_title('Series plot (from COMPUTATION)')
df = pd.DataFrame(rows_list)
print(df)

#%% Extract data from dataframe
OTDRX = df['OTDRX'][2]
OTDRY = df['OTDRY'][2]
print(f'OTDRX: {OTDRX}')
fig, ax = plt.subplots( 1,1, figsize=(12,9), sharex=False)  #W x H
plt.plot(OTDRX, OTDRY)
assert isinstance(ax, matplotlib.axes._subplots.Subplot) # for pop-up type-hinting in pycharm
ax.set_title('OTDR plot (data read from DATAFRAME)')

#%% Save data to CSV
data_path = Path(Path(__file__)).parent
filename = "Array_in_Pandas.csv"
full_filename = Path(data_path, filename)
print(data_path)
df.to_csv(full_filename, index=False)

#%% Data read from FILE

# Load file, format dataframe
print('loading')
print(f'*** LOADING: Filename: {filename}')
df2 = pd.read_csv(full_filename, delimiter=',')  # , index_col = 'Timestamp')
# Set the index
df2.set_index(pd.DatetimeIndex(df['Timestamp']),
              inplace=True
              )  # ref: https://stackoverflow.com/questions/27032052/how-do-i-properly-set-the-datetimeindex-for-a-pandas-datetime-object-in-a-datafr
print(f"Index type is {type(df2.index)}")  # ought to be a DatetimeIndex type now,

# Print column names
print(f'column names = {df2.columns.values}')

OTDRX = df2['OTDRX'][2] # Read in 3rd row
OTDRY = df2['OTDRY'][2]

otdrx = np.fromstring(   OTDRX[1:-1], sep =' ', dtype=float)
otdry = np.fromstring(   OTDRY[1:-1], sep =' ', dtype=float)

# one-liner
#otdrx = np.fromstring(  df2['OTDRX'][2][1:-1] , sep =' ').astype(float)
#otdry = np.fromstring(  df2['OTDRY'][2][1:-1] , sep =' ').astype(float)

fig, ax = plt.subplots( 1,1, figsize=(12,9), sharex=False)  #W x H
plt.plot(otdrx, otdry, '-ro')
ax.set_title('OTDR plot (data read from CSV FILE)')

