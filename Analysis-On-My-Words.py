
from matlablib import *
import pandas as pd
from pandas import DataFrame
# 'pip install nb2xls ' - EXCEL reference; https://towardsdatascience.com/jupyter-is-the-new-excel-but-not-for-your-boss-d24340ebf314
import os
import matplotlib.pyplot as plt
import sys

##
# TODO
# - ALT+4, CTRL+W to close current window
# - CTRL+W is currently expand,
# - CTRL+D jump to definition (Currently CTRL+B)

##
fname='words.xlsx'
cwd= os.getcwd() # current working directory

Fname=os.path.join(cwd, fname)
df = pd.read_excel (Fname, header=None, sheet_name='Sheet1', names=['order', 'word']) #for an earlier version of Excel, you may need to use the file extension of 'xls'
# df.rename(columns={"Entry_Order": "col1", "Word":"verd"}) # Must be a dictionary

# Adjust case - note in-place overwrite
df['word'] = df['word'].str.upper() # Convert all to caps
df['word'] = df['word'].str.capitalize()

df=df.sort_values('word') # Sort in descending order
df.head(5) # print first few lines
df.tail(5)# print last few lines

#df['firstLetter'] = df['word'].astype(str).str[0] # AStype to COERCE to a string
df['firstLetter'] = df['word'].str[0] # Create new column with the first letter from the 'word' column


# Using counts function that will analyze the occurrene of given letters - will return a Series
df2=df['firstLetter'].value_counts() # Returns a series
df2=df2.sort_index() # sorted list of letters...still a seris
df3=DataFrame(df2) #, columns=['letters'])  # Change our new series into a dataframe to access methods

df3['index_col'] = range(1, len(df3) + 1) #Create index column with enumerated rows - name it 'index_col'
df3['Letters']=df3.index # copy the letters to a unique column
df3.index=df3['index_col'] # set index_column to be the indes


df3 = df3.drop('index_col', 1)  # where 1 is the axis number (0 for rows and 1 for columns.)
df3=df3.rename(columns={'word':'counts'})

# %df = DataFrame(Data,columns=['Unemployment_Rate','Stock_Index_Price'])
# df2['numbers']

print('Analysis complete on wordcount')


for i, word in enumerate(df['word']):
    my_string=f'{i}, {word}'
    print(my_string)

# keyboard()           # drop to console in this sesstion
# sys.exit(0)         # Really terminate the python console


## Figure
# df3.plot(x =df3.index.values, y='counts', kind = 'scatter')
# x=df3.index.values
# y=df3['counts'].values
#
# plt.plot(x,y)
# plt.xticks( df3['Letters'], df3.index.values )
# plt.show()

## DROP TO KEYBOARD, ref: https://stackoverflow.com/questions/2158097/drop-into-python-interpreter-while-executing-function
# ref: https://thepythonguru.com/python-builtin-functions/locals/ (VERY INTERSTING
# https://www.digitalocean.com/community/tutorials/how-to-debug-python-with-an-interactive-console  <--  INTERSTIN

# import code
# print('code.interact started')
# #code.interact(local=locals())
# code.interact(banner='WELCOME, CTRL+Z to return', readfunc=None, local=locals(), exitmsg='..now returning to script')
# print('returned from code.interact!')  # Not sure how to quit the code interact secssion

# NOTE: I had trouble ever returning from this in pycharm. IPython worked perfectly. So use this.




## other notes
# ## Make a dataframe out of a series
#
# ##
#
#
# letter=df['word'].str.get(0)
#
# df['word'].get(33)
# letter # dataframe of all letters
#
# # TODO Insert the letters as a new dataframe column
#
# ##
# print('cell 1')
# df2=df['firstLetter'].value_counts()
#
# ##
# df.word.count()
# wordlist=df.word.values
#
# capitalize(word) for word in wordlist:
#     print(word)
#
# # [x] for word in wordlist
#
# x = [i for i in range(10)] # list comprehension to return a list
#
# ## Generalized capitals
# capitalizedWords=[str.capitalize((word)) for word in wordlist] # This is a list
# capitalizedWords.sort() # in-place modification
#
# # TOTO: would have been cool to do this in place inside the pandas object


