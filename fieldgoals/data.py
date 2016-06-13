import requests
from lxml import html 
import numpy as np
import urllib
from bs4 import BeautifulSoup
import csv
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

def get_teams():
	base_url='http://espn.go.com/nba/statistics/team/_/stat/offense/sort/points/year/2015/seasontype/2/split/'
	team_urls=[base_url+str(x) for x in xrange(31)][1::]
	fg_matrix=np.zeros(shape=(30,30))
	for url in team_urls:
		page=requests.get(url)
		tree=html.fromstring(page.content)
		table=tree.xpath('//*[@id="my-teams-table"]/div/div[2]/table/tr')
		comparison_team=find_opponent(url, tree)
		comparison_teams_index=team_names.index(comparison_team)
		#We now have the data for the page, now to loop through the teams on the page
		for row in table:
			name=row.xpath('td[2]/a/text()')
			if name == []:
				pass
			else:
				name=name[0]
				name_index=team_names.index(name)
				fg=row.xpath('td[6]/text()')[0]
				print("Row")
				fg_matrix[name_index][comparison_teams_index]=fg
	np.fill_diagonal(fg_matrix, -1)
	np.savetxt("data.csv", fg_matrix, delimiter=",", fmt='%.3f')

def find_opponent(url, tree):
	comparison_teams=tree.xpath('//*[@id="content"]/div[2]/div/div/div[4]/form[2]/select/option')[2:32]
	comparison_teams_names=[team.xpath('text()')[0] for team in comparison_teams]
	comparison_teams_urls=[team.xpath('@value')[0] for team in comparison_teams]
	index=comparison_teams_urls.index(url)
	opponent_team=comparison_teams_names[index]
	index_period=opponent_team.index('.')
	opponent_team=opponent_team[index_period+2::]
	return opponent_team

get_teams()