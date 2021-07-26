import csv
import re

def mod_date(string_date):
    split_date = re.split(', | ',string_date)
    if split_date[0] == 'January':
        return '01-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'February':
        return '02-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'March':
        return '03-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'April':
        return '04-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'May':
        return '05-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'June':
        return '06-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'July':
        return '07-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'August':
        return '08-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'September':
        return '09-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'October':
        return '10-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'November':
        return '11-'+split_date[1]+'-'+split_date[2]
    if split_date[0] == 'December':
        return '12-'+split_date[1]+'-'+split_date[2]

# open file in read mode
with open('../original_data/gun_violence_stats/concatenated-gun-incidents14-18.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_dict_reader = csv.DictReader(read_obj)
    # Iterate over each row in the csv using reader object
    output_list = []
    for row in csv_dict_reader:
        modified_date = mod_date(row['Incident Date'])
        output_list.append({'date': modified_date, 'value': row['# Killed'] + row['# Injured']})
    
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
