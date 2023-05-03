# csv
import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})
    writer.writerow({'Name': 'B', 'Count': 3})
    writer.writerow({'Name': 'B', 'Count': 4})
    writer.writerow({'Name': 'B', 'Count': 5})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])