# %%
import pandas as pd


# %% Load
df = pd.read_csv("words.txt", delimiter="\n", names=["WORDS"])

print("1")
df["WORDS"] = df["WORDS"].str.strip()
df["WORDS"] = df["WORDS"].str.capitalize()

df.sort_values("WORDS", ascending=True, inplace=True)

print("2")
print("Described              :---------------------")
print(df.describe())
print("Showing duplicated rows:---------------------")
dupes = df[df.duplicated(keep=False)]
print("donnny")


# %%
for i, dupe in enumerate(dupes["WORDS"].items()):
    print(f"{i}: {dupe}")

# %% Unique elements
print("\n\n\n Now priingtin unique elements \n\n")
uniques = df["WORDS"].unique()
for element in uniques:
    print(f"{element}")

# %%
print("doggnney")


# %%
