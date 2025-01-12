import csv
import os

# Define paths
base_path = '/Users/Rebin/Documents/Wallapper_Group_Website/To Github/pdf'
csv_file_path = os.path.join(base_path, 'file_mapping.csv')
sets = ['set1', 'set2', 'set3']

# Create a dictionary to map file names to their sets
file_to_set = {}

# Populate the dictionary with files from each set
for set_name in sets:
    set_path = os.path.join(base_path, set_name)
    for file_name in os.listdir(set_path):
        if file_name.endswith('.pdf'):
            file_base_name = os.path.splitext(file_name)[0]
            file_to_set[file_base_name] = set_name

# Read the CSV file and update rows with set information
updated_rows = []
with open(csv_file_path, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames + ['set']  # Add a new 'set' column
    for row in reader:
        pattern = row['pattern']  # Adjust 'pattern' if the column name is different
        if pattern in file_to_set:
            row['set'] = file_to_set[pattern]
        updated_rows.append(row)

# Write the updated rows back to the CSV
with open(csv_file_path, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(updated_rows)

print("CSV file updated to include set information for each PDF.")
