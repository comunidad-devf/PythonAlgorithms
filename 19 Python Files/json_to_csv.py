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
    file_list = [file_in.split('.')[0], 'csv']
    file_out = ".".join(file_list)

file_work = open(file_in)
data = json.load(file_work)
file_work.close()

with open(file_out, "wb+") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(data[0].keys())
    for item in data:
        csv_file.writerow(item.values())
