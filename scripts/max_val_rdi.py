import csv

max_val = float(0.0)
with open('RDI-99-2021.csv', 'r') as read_obj:
    csv_reader = csv.DictReader(read_obj)
    for row in csv_reader:
        if float(row['DSPIC96']) > max_val:
            max_val = float(row['DSPIC96'])
    print(max_val)