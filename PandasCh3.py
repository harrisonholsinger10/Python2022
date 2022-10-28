import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv', sep='\t')

fig = plt.figure()

movement = df.loc[(df['year'] == 1952)]
movement2 = df.loc[(df['year'] == 2007)]

f, axs = plt.subplots(1,2, figsize=(9,5),sharey=True)

ax = sns.scatterplot(x='lifeExp', y='gdpPercap', data= movement, hue = "continent", ax=axs[0], legend = False)
ax.set_title('1952')
ax.set_xlabel('Life Expectancy')
ax.set_ylabel('GDP Per Capita')


ax2 = sns.scatterplot(x='lifeExp', y='gdpPercap', data=movement2, hue = "continent", ax=axs[1])
ax2.set_title('2007')
ax2.set_xlabel('Life Expectancy')
ax2.set_ylabel('GDP Per Capita')
f.suptitle('Life Expectancy vs. GDP Per Capita', fontsize=16)







