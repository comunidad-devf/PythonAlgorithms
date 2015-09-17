import csv

list1 = [1, 2, 3, 4, 5]

output = open('csv.csv', 'wb')
wr = csv.writer(output, quoting=csv.QUOTE_ALL)
wr.writerow(list1)
