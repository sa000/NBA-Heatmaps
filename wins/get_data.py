import requests
from lxml import html 
import numpy as np
import urllib
from bs4 import BeautifulSoup
import csv
import seaborn as sns
def get_teams(url):
	base_url='https://www.teamrankings.com'
	page=requests.get(url)
	tree=html.fromstring(page.content)
	teams=tree.xpath('//*[@id="html"]/body/div[3]/div[1]/div[3]/div/ul/li[9]/ul/li')
	team_name=[]
	team_url=[]
	for team in teams:
		team_name.append(team.xpath('a/text()')[0])
		team_url.append(base_url+team.xpath('a/@href')[0])
	return team_name, team_url

def grab_records(teams, urls):
	cities=[]
	target=open('data.csv', 'w')
	for team in teams:
		team=team.split(' ')
		cities.append(" ".join(team[0:len(team)-1]))
  #   	print('hi')
  #   	print(" ".join(team[0:last]))
  	cities[12]='LA Clippers'
  	cities[13]='LA Lakers'
  	cities[20]='Okla City'
  	cities[24]='Portland'
	record_matrix=np.zeros(shape=(30,30))
	win_matrix=np.zeros(shape=(30,30))
	record_percentage=np.zeros(shape=(30,30))

	for index, url in enumerate(urls):

		wins=np.zeros(30)
		games=np.zeros(30)
		losses=np.zeros(30)
		win_percentage=np.zeros(30)
		print(url)
		page = urllib.urlopen(url)
		soup=BeautifulSoup(page,"lxml")
		table=soup.findAll('table')[1] 
		rows=table.findAll('tr')
		for entry, row in enumerate(rows[1:83]):
			stats=row.findAll('td')
			opponent=stats[1].text
			outcome=stats[2].text[0]
			opp_index=cities.index(opponent)
			games[opp_index]+=1
			if outcome=='L':
				losses[opp_index]+=1
			else:
				wins[opp_index]+=1
			win_percentage[opp_index]=wins[opp_index]/games[opp_index]
		record_matrix[index]=win_percentage*100
		win_matrix[index]=wins
	np.fill_diagonal(record_matrix,-1)
	with open('data.csv', 'wb') as datacsv:
		csvwriter=csv.writer(datacsv)
		for row in record_matrix:
			csvwriter.writerow(row)
	with open('wins.csv', 'wb') as datacsv:
		csvwriter=csv.writer(datacsv)
		for row in win_matrix:
			csvwriter.writerow(row)
	return(record_matrix)

if __name__ == '__main__':
	teams, urls=get_teams('https://www.teamrankings.com/nba/team/atlanta-hawks/')
	record_matrix=grab_records(teams,urls)