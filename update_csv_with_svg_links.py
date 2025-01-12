import csv

# File paths
main_csv_path = '/Users/Rebin/Documents/Wallapper_Group_Website/To Github/pdf/file_mapping.csv'

# Read the main CSV
with open(main_csv_path, mode='r', newline='') as main_csv:
    reader = csv.reader(main_csv)
    headers = next(reader)
    main_data = list(reader)

# Write updated data back to the main CSV
with open(main_csv_path, mode='w', newline='') as main_csv:
    writer = csv.writer(main_csv)
    writer.writerow(headers)
    for row in main_data:
        # Remove '@' from github_pdf_url and github_csv_url
        row[-2] = row[-2].lstrip('@')  # github_pdf_url
        row[-1] = row[-1].lstrip('@')  # github_csv_url
        writer.writerow(row)

print("Removed '@' from github_pdf_url and github_csv_url columns.") 