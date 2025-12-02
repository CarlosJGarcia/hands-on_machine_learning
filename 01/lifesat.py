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

print("Fin del programa.")
