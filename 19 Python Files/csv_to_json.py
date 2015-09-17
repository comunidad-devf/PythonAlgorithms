"""Convert CSV into JSON file."""

import csv
import json
import os
import sys

if len(sys.argv) < 2:
    sys.exit('Debes agregar un argumento')
file_in = sys.argv[1]
file_only = os.path.basename(file_in)

try:
    file_out = sys.argv[2]
except:
    file_list = [file_only.split('.')[0], 'json']
    file_out = ".".join(file_list)

data = csv.reader(open(file_in, 'rU'), delimiter=',')

field_names = data.next()

field_names_len = len(field_names)

json_list = []
i = 0

for row in data:
    json_list.append({})

    for j in range(0, len(row)):
        json_list[i][field_names[j]] = row[j]

    for j in range(len(row), field_names_len):
        json_list[i][field_names[j]] = ""

    i = i + 1

with open(file_out, 'w') as outfile:
    json.dump(json_list, outfile, sort_keys=True, indent=4, ensure_ascii=False)
sys.exit()
