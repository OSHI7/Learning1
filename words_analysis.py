
#%%
import pandas as pd


#% Load
df = pd.read_csv('words.txt', delimiter='\n', names=['WORDS'])

df['WORDS'] = df['WORDS'].str.strip()
df['WORDS'] = df['WORDS'].str.capitalize()

df.sort_values('WORDS', ascending=True, inplace=True)
print('Described              :---------------------')
df.describe()
print('Showing duplicated rows:---------------------')
dupes = df[df.duplicated(keep=False)]


#%%
for i, dupe in enumerate(dupes['WORDS'].items()):
    print(f"{i}: {dupe}")

# %% Unique elements
uniques = df.unique
for element in uniques['WORDS'].items():
    print(f"{element}")
# %%
