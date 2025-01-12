import csv
import os

# Define paths
base_path = '/Users/Rebin/Documents/Wallapper_Group_Website/To Github/pdf'
csv_file_path = os.path.join(base_path, 'file_mapping.csv')

# Read the CSV file and add SVG links
updated_rows = []
with open(csv_file_path, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames + ['svg_path']  # Add a new 'svg_path' column
    for row in reader:
        pdf_path = row['pdf_path']  # Use 'pdf_path' as the column name
        svg_path = pdf_path.replace('.pdf', '.svg')
        row['svg_path'] = svg_path
        updated_rows.append(row)

# Write the updated rows back to the CSV
with open(csv_file_path, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(updated_rows)

print("CSV file updated to include SVG paths.") 