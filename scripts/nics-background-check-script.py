import csv
# open file in read mode
with open('EDITED-nics-firearm-background-checks.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_dict_reader = csv.DictReader(read_obj)
    # Iterate over each row in the csv using reader object
    new_dict = {}
    for row in csv_dict_reader:
        if row['month'] in new_dict.keys():
            new_dict[row['month']] += int(row['totals'])
        else:
            new_dict[row['month']] = int(row['totals'])

    output_list = []
    for entry in new_dict:
        output_list.append({'date': entry, 'value': new_dict[entry]})

csv_columns = ['date', 'value']
with open('massaged-nics-firearm-background-checks.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in output_list:
        writer.writerow(data)
