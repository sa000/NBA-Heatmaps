import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="white")
records=np.zeros(shape=(30,30))
with open('data.csv') as datacsv:
	datacsv=csv.reader(datacsv)
	for index, row in enumerate(datacsv):
		records[index]=row
rc={

}
columns=['ATL',
 'BOS',
 'BKN',
 'CHA',
 'CHI',
 'CLE',
 'DAL',
 'DEN',
 'DET',
 'GSW',
 'HOU',
 'IND',
 'LAC',
 'LAL',
 'MEM',
 'MIA',
 'MIL',
 'MIN',
 'NOP',
 'NYK',
 'OKC',
 'ORL',
 'PHL',
 'PHO',
 'POR',
 'SAC',
 'SAN',
 'TOR',
 'UTA',
 'WAS']

df=pd.DataFrame(records, index=columns, columns=columns)
mask=df<0
fig = sns.heatmap(df, vmin=0, vmax=100,linewidths=.5, cmap="coolwarm", mask=mask,fmt='.2f')

fig.set_title("NBA team win matrix")
sns.color_palette("coolwarm", 4)
plt.yticks(rotation=0)
plt.xticks(rotation=90)

fig=fig.get_figure()
fig=fig.savefig('testing.png')
