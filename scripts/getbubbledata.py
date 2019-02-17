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

f = open("bubbledata.json", "a")

for t in countries.items():
     f.write(json.dumps({"Name":t[0], "Count":t[1]}) + ",\n")