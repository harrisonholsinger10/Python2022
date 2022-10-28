# Harrison Holsinger

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv', sep='\t')

continent_df = df['continent']

df ['continent'] = df ['continent'].astype(str)

df2 = df.loc[df['continent'] == ('Americas')] 

meanLifeExpectancy = df2 ['lifeExp'].mean() 

print(meanLifeExpectancy)

df2 = df2.groupby('year')['lifeExp'].mean()

print(df2.plot(color = 'Red', 
               xlabel='Year', 
               ylabel='Average Life Expectancy', 
               title='Average Life Expectancy per Year in the Americas', 
               grid = True))
