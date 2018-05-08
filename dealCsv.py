import csv

filename = '/Users/ruiguang.sun/test.csv'
with open(filename) as f:
    reader = csv.reader(f)
    print(list(reader))