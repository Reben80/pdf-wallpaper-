import csv
import os

# Define paths
base_path = '/Users/Rebin/Documents/Wallapper_Group_Website/To Github/pdf'
csv_file_path = os.path.join(base_path, 'file_mapping.csv')
sets = ['set1', 'set2', 'set3']

# Count the number of rows in the CSV file
with open(csv_file_path, mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    csv_row_count = sum(1 for row in reader) - 1  # Subtract 1 for the header

# Count the total number of PDF files
pdf_count = 0
for set_name in sets:
    set_path = os.path.join(base_path, set_name)
    pdf_count += len([file for file in os.listdir(set_path) if file.endswith('.pdf')])

print(f"Number of rows in CSV (excluding header): {csv_row_count}")
print(f"Total number of PDF files: {pdf_count}")