import pandas as pd
import json
import itertools
from operator import itemgetter
import operator

df = pd.read_csv("..\data\dataset.csv")
one = df.country1
rounds = df['round']
players = df['player1']

c_list = list()
r_list = list()
p_list = list()
countries = dict()

for c in one:
    c_list.append(c)

for r in rounds:
    r_list.append(r)

for p in players:
    p_list.append(p)

# c_list = list(set(c_list))

for country, rou, play in zip(c_list, r_list, p_list):

        if country not in countries:
            countries[country] = {}
        points = 0

        if rou == "First":
            points += 1
        elif rou == "Second":
            points += 2
        elif rou == "Third":
            points += 4
        elif rou == "Fourth":
            points += 8
        elif rou == "quater":
            points += 16
        elif rou == "semi":
            points += 32
        elif rou == "final":
            points += 64

        countries[country][play] = countries[country].get(play, 0) + points

# print json.dump(countries["IND"])

# print countries
# f = open("../data/Countries/test.json", "a")
# f.write(json.dumps(countries["IND"]))

# country_unique_list = list(set(c_list))
# f = open("../data/countrylist.json", "a")
# json_data = json.dumps(country_unique_list)
# f.write(json_data)

for country in country_unique_list:
    f = open("../data/Countries/" + country + ".json", "a")
    sorted_country = sorted(countries[country].items(), key=operator.itemgetter(1), reverse=True)
    f.write(json.dumps(sorted_country))