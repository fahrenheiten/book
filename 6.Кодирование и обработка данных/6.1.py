# import csv
# with open('stocks.csv') as file:
#     fale_csv = csv.reader(file)
#     headers = next(fale_csv)
#     for i in fale_csv:
#         print(i)

# import csv
# from collections import namedtuple
# with open('stocks.csv') as file:
#     file_csv = csv.reader(file)
#     headers = next(file_csv)
#     Row = namedtuple('Row', headers)
#     for i in file_csv:
#         row = Row(*i)
#         print(i)

import csv
# with open('stocks.csv') as file:
#     file_csv = csv.DictReader(file)
#     for row in file_csv:
#         print(row)

import csv
with open('stocks.csv') as file:
    file_tsv = csv.reader(file,delimiter = '\t')
    for row in file_tsv:
        print(row)