import pandas as pd
df = pd.read_csv("..\data\dataset.csv")
one = df.country1
two = df.country2

c1 = list()
c2 = list()
countries = dict()

for c in one:
      countries[c] = countries.get(c, 0) + 1
print countries