# 'pip install nb2xls ' - EXCEL reference; https://towardsdatascience.com/jupyter-is-the-new-excel-but-not-for-your-boss-d24340ebf314

import pandas as pd
import os

##
fname='words.xlsx'
cwd= os.getcwd() # current working directory

Fname=os.path.join(cwd, fname)
df = pd.read_excel (Fname, header=None, sheet_name='Sheet1', names=['order', 'word']) #for an earlier version of Excel, you may need to use the file extension of 'xls'
# df.rename(columns={"Entry_Order": "col1", "Word":"verd"}) # Must be a dictionary
df=df.sort_values('word') # Sort in descending order
df.head(5) # print first few lines
df.tail(5)# print last few lines



##


letter=df['word'].str.get(0)

df['word'].get(33)
letter # dataframe of all letters

# TODO Insert the letters as a new dataframe column
##
print('cell 1')


##
df.word.count()





print(i) for i in df.['word']:






