# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression


# Load the CSV data from file into a pandas.DataFrame
file = 'data/lifesat.csv'
lifesat_df = pd.read_csv(file)

# Show the headers and the first 3 lines of the DataFrame
print(lifesat_df.head(3))

gdps = lifesat_df["GDP per capita (USD)"].tolist()
satisfactions = lifesat_df["Life satisfaction"].tolist()

n = 0
for gdp in gdps:
    print(f"{n} : {gdp}")
    n += 1
    if n > 3: break

n = 0
for satisfaction in satisfactions:
    print(f"{n} : {satisfaction}")
    n += 1
    if n > 3: break


"""
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

print("x:", x)
print("y:", y)



import csv
from pathlib import Path

path = Path('data/lifesat.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(f"[{index}] {column_header}", end=" / ")
print()

countries = []
for row in reader:
    country = row[0]
    countries.append(country)

for n, country in enumerate(countries):
    print(f"{n}: {country}")
"""
    
print("Fin del programa.")
