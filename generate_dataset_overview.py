import json
import csv
import os

def process_json_files(json_folder, csv_filename):
    data_list = []
    # all_keys = set()
    all keys = [
        'name',
        'alternateName',
        'type',
        'version',
        'creator_affiliation',
        'creater_name',
        'creater_orcid',
        'description',
        'keywords',
        'dateCreatede',
        'doi',
        'datePublished',
        'licence',
        'comment',
        'citation',
        'doiRequest',
    ]

    for filename in os.listdir(json_folder):
        if filename.endswith(".json"):
            with open(os.path.join(json_folder, filename), 'r') as json_file:
                try:
                    data = json.load(json_file)
                    # Flatten the JSON structure
                    flattened_data = flatten_json(data)
                    # Add flattened data to the list
                    data_list.append(flattened_data)
                    # Update the set of all keys
                    all_keys.update(flattened_data.keys())
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")

    # Write the data to a CSV file
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(all_keys)
        # Write data
        for data_row in data_list:
            csv_writer.writerow([data_row.get(key, '') for key in all_keys])

def flatten_json(json_data, parent_key='', sep='_'):
    flattened_data = {}
    for k, v in json_data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flattened_data.update(flatten_json(v, new_key, sep=sep))
        else:
            flattened_data[new_key] = v
    return flattened_data

if __name__ == "__main__":
    process_json_files("metadata", "overview_available_datasets.csv")
