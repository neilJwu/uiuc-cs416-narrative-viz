import csv

max_val = 0
with open('monthly-gun-violence14-18.csv', 'r') as read_obj:
    csv_reader = csv.DictReader(read_obj)
    for row in csv_reader:
        if int(row['value']) > max_val:
            max_val = int(row['value'])
    print(max_val)