import csv
import os

# Define paths
base_path = '/Users/Rebin/Documents/Wallapper_Group_Website/To Github/pdf'
csv_file_path = os.path.join(base_path, 'file_mapping.csv')
sets = ['set1', 'set2', 'set3']

# Collect all existing PDF file names (without extension)
existing_files = set()
for set_name in sets:
    set_path = os.path.join(base_path, set_name)
    for file_name in os.listdir(set_path):
        if file_name.endswith('.pdf'):
            file_base_name = os.path.splitext(file_name)[0]
            existing_files.add(file_base_name)

# Read the CSV file and filter rows
filtered_rows = []
with open(csv_file_path, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    for row in reader:
        if row['pattern'] in existing_files:  # Adjust 'pattern' if the column name is different
            filtered_rows.append(row)

# Write the filtered rows back to the CSV
with open(csv_file_path, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(filtered_rows)

print("CSV file updated to remove entries without associated PDF files.") 