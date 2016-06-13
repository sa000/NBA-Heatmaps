import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="white")

fg_matrix=np.genfromtxt('data.csv', delimiter=",")

team_names=["Atlanta",
"Boston",
"Brooklyn",
"Charlotte",
"Chicago",
"Cleveland",
"Dallas",
"Denver",
"Detroit",
"Golden State",
"Houston",
"Indiana",
"LA Clippers",
"LA Lakers",
"Memphis",
"Miami",
"Milwaukee",
"Minnesota",
"New Orleans",
"New York",
"Oklahoma City",
"Orlando",
"Philadelphia",
"Phoenix",
"Portland",
"Sacramento",
"San Antonio",
"Toronto",
"Utah",
"Washington"]

df=pd.DataFrame(fg_matrix, index=team_names, columns=team_names)
mask=df<0
fig = sns.heatmap(df, vmin=.20, vmax=.60, cmap="coolwarm", linewidths=.5, mask=mask, center=np.average(fg_matrix))

fig.set_title("NBA Field Goal Matrix")
plt.yticks(rotation=0)
plt.xticks(rotation=90)

fig=fig.get_figure()
fig.tight_layout()
fig=fig.savefig('testing.png')