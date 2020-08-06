import requests
from bs4 import BeautifulSoup



nbaGamesList = []
fullNbaName = []
nbaAbvList = []
links = []
logos = []

# GET LINKS FROM PARENT WEBSITE (WORKS)
source = requests.get('http://nba-streams.xyz/schedule/').text
soup = BeautifulSoup(source, 'html.parser')

for a in soup.find_all('a', href=True):

    links.append(a['href'])
del links[0]


# TODO: ITERATE THROUGH EACH STREAM AND GET .TS

for nbaStream in links:
    stream = requests.get(nbaStream).text
    s = BeautifulSoup(stream, 'html.parser')

    # Get Logo Address
    logo = s.find_all('img')[0]['src']

    temp = logo.split('/')[2]
    svg = temp.split('.')[0]
    if (len(svg) > 10):
        comb = svg.split('-')[1]
        comb2 = svg.split('-')[2]
        name = comb + ' ' + comb2
    else:
        name = svg
    fullNbaName.append(name)
    logo = 'http://nba-streams.xyz/nba' + logo
    # print(logo)
    logos.append(logo)

    # Get Nba Abv
    php = s.find_all('iframe')[0]['src']
    nbaAbv = php.split('/')[4]
    prefix = 'la'
    nbaAbvList.append(nbaAbv)

    # Get Full Team Name


    # Concatenate all Lists for east access (Full Nba Name, StreamLink, Logo, Abv)

for x in range(len(fullNbaName)):
    nbaGames = []
    nbaGames.append(fullNbaName[x])
    # Need streamLink
    nbaGames.append(logos[x])
    nbaGames.append(nbaAbvList[x])

    nbaGamesList.append(nbaGames)

