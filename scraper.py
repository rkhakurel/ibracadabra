from bs4 import BeautifulSoup
import requests

url = 'https://stats.espncricinfo.com/ci/content/records/83548.html'

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, features='html5lib')

stat_counter = 1
rank_counter = 1
rank = []
player = []
span = []
mat = []
inns = []
no = []
runs = []
hs = []
ave = []
bf = []
sr = []
hundreds = []
fifties = []
zeroes = []
fours = []
sixes = []

for stat in soup.findAll("td", {"nowrap": "nowrap"}):
    if stat_counter % 15 == 1:
        rank.append(rank_counter)
    if stat_counter % 15 == 1:
        player.append(stat.text)
    elif stat_counter % 15 == 2:
        span.append(stat.text)
    elif stat_counter % 15 == 3:
        mat.append(stat.text)
    elif stat_counter % 15 == 4:
        inns.append(stat.text)
    elif stat_counter % 15 == 5:
        no.append(stat.text)
    elif stat_counter % 15 == 6:
        runs.append(stat.text)
    elif stat_counter % 15 == 7:
        hs.append(stat.text)
    elif stat_counter % 15 == 8:
        ave.append(stat.text)
    elif stat_counter % 15 == 9:
        bf.append(stat.text)
    elif stat_counter % 15 == 10:
        sr.append(stat.text)
    elif stat_counter % 15 == 11:
        hundreds.append(stat.text)
    elif stat_counter % 15 == 12:
        fifties.append(stat.text)
    elif stat_counter % 15 == 13:
        zeroes.append(stat.text)
    elif stat_counter % 15 == 14:
        fours.append(stat.text)
    elif stat_counter % 15 == 0:
        sixes.append(stat.text)
        rank_counter += 1
    stat_counter += 1

print(rank, player, span, mat, inns, no, runs, hs, ave, bf, sr, hundreds, fifties, zeroes, fours, sixes, sep='\n')
