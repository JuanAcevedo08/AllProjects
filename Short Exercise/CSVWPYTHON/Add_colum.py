import csv

main_file = 'bike.csv'
new_file = 'products_motos_update.csv'

with open(main_file, mode='r')as main_file:
    csv_reader = csv.DictReader(main_file)
    fieldname = csv_reader.fieldnames + ['totally_name']

    with open(new_file, mode='w', newline='')as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldname)
        csv_writer.writeheader()
        for row in csv_reader:
            row['totally_name'] = str(row['brand']) + ' ' + str(row['name'])
            csv_writer.writerow(row)