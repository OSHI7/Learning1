
import pandas as pd
# 'pip install nb2xls ' - EXCEL reference; https://towardsdatascience.com/jupyter-is-the-new-excel-but-not-for-your-boss-d24340ebf314
import os
import matplotlib.pyplot as plt

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
df2=df['firstLetter'].value_counts() # Returns a series

df2=df2.sort_index() # sorted list of letters returned as a series.
df2['numbers']

## Figure
df2.plot(x ='index', y='Stock_Index_Price', kind = 'scatter')

##
df2 = DataFrame(Data,columns=['Unemployment_Rate','Stock_Index_Price'])
##


letter=df['word'].str.get(0)

df['word'].get(33)
letter # dataframe of all letters

# TODO Insert the letters as a new dataframe column

##
print('cell 1')
df2=df['firstLetter'].value_counts()

##
df.word.count()
wordlist=df.word.values

capitalize(word) for word in wordlist:
    print(word)

# [x] for word in wordlist

x = [i for i in range(10)] # list comprehension to return a list

## Generalized capitals
capitalizedWords=[str.capitalize((word)) for word in wordlist] # This is a list
capitalizedWords.sort() # in-place modification

# TOTO: would have been cool to do this in place inside the pandas object


