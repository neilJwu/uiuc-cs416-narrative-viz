import csv

# open file in read mode
with open('../massaged_data/massaged-nics-firearm-background-checks.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_dict_reader = csv.DictReader(read_obj)
    # Iterate over each row in the csv using reader object
    output_list = []
    for row in csv_dict_reader:
        output_list.append({'date': row['date'], 'value': row['value']})
    
    final_output = []
    for i in reversed(range(1, len(output_list))):
        print("Comparing difference between " + output_list[i-1]['date'] + " and " + output_list[i]['date'])
        final_output.append({'later_date': output_list[i-1]['date'], 'earlier_date': output_list[i]['date'], 'diff': int(output_list[i-1]['value'])-int(output_list[i]['value'])})
   
    newlist = sorted(final_output, key=lambda k: k['diff'])
    print(newlist[-10:])