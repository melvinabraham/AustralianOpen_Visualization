import pandas as pd
import json
import itertools
from operator import itemgetter
import operator

df = pd.read_csv("..\data\dataset.csv")
one = df.country1
rounds = df['round']

c_list = list()
r_list = list()
countries = dict()

for c in one:
    c_list.append(c)

for r in rounds:
    r_list.append(r)

for country, rou in zip(c_list, r_list):
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

    countries[country] = countries.get(country, 0) + points

# sorted_x = sorted(countries.items(), key=operator.itemgetter(1), reverse=1)

f = open("jsondata.json", "a")

for t in countries.items():
     f.write(json.dumps({"Name":t[0], "Count":t[1]}) + ",\n")


# print sorted_x

# for c in one:
#       points = 0
#       countries[c] = countries.get(c, 0) + 1

# for keys in countries:
    # tup = {"Name":keys, "Count": countries[keys]}
    # print json.dumps(tup) + ","
    # sorted(tup, key = 'Count')
    # items = sorted(tup.iteritems(), key=lambda x: x[1].Count, reverse=True)
    # print items
    
# tup = sorted(tup, key = itemgetter('Count'), reverse=True)
# print tup
# 
