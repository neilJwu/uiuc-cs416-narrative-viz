import csv

max_val = 0
with open('../massaged_data/massaged-gun-violence14-18.csv', 'r') as read_obj:
    csv_reader = csv.DictReader(read_obj)
    new_dict={}
    for row in csv_reader:
        month_year = row['date'].split("-")[0] + "-" + row['date'].split("-")[1]
        if month_year in new_dict.keys():
            new_dict[month_year] += int(row['value'])
        else:
            new_dict[month_year] = int(row['value'])
      
    second_output_list = []
    for entry in new_dict:
        second_output_list.append({'date': entry, 'value': new_dict[entry]})
    
csv_columns = ['date', 'value']
with open('../massaged_data/monthly-gun-violence14-18.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in second_output_list:
        writer.writerow(data)
