import csv
import re

# open file in read mode
with open('../original_data/gun_violence_stats/gun-violence-data_01-2014_03-2018.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_dict_reader = csv.DictReader(read_obj)
    # Iterate over each row in the csv using reader object
    output_list = []
    for row in csv_dict_reader:
        output_list.append({'date': row['date'], 'value': row['n_killed'] + row['n_injured']})
    
    new_dict = {}
    for element in output_list:
        if element['date'] in new_dict.keys():
            new_dict[element['date']] += int(element['value'])
        else:
            new_dict[element['date']] = int(element['value'])
    
    second_output_list = []
    for entry in new_dict:
        second_output_list.append({'date': entry, 'value': new_dict[entry]})
    
csv_columns = ['date', 'value']
with open('../massaged_data/massaged-gun-violence14-18.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in second_output_list:
        writer.writerow(data)
