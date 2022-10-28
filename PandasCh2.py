import pickle
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv', sep='\t')

df.to_pickle("mydataframe.pickle")

df_pickle = pd.read_pickle("mydataframe.pickle")

print(df_pickle.head())