#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: csv_to_json
# date: "2023-05-06"

import csv
import json
import os

json_file_path = 'index.json'
tagnames_file_path = 'tagnames.json'
cwd = os.getcwd()
folder_name = os.path.basename(cwd)


def open_csv_file(csv_file_path):

    # Open the CSV file and read its contents
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Get the header row

        # Store the original header in a dictionary
        tags_dict = {}
        for i in range(len(header)-1):
            tags_dict[str(i)] = header[i+1]

        # Create a new header with values "0" and "1"
        new_header = ["0", "1", "2"]

        # Convert each row to a dictionary
        data_dict = {}
        for row in csv_reader:
            key = row[0].zfill(3)  # Pad the key with leading zeros
            data_dict[folder_name + key] = {new_header[i]: row[i+1] for i in range(len(new_header))}

    # Write the resulting dictionary as JSON
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data_dict, jsonfile, ensure_ascii=False, indent=4, separators=(',', ': '))

        # Add a newline character after each item in the JSON output
        jsonfile.write('\n')

    # Write the original header as a separate JSON file
    with open(tagnames_file_path, 'w', encoding='utf-8') as tagsfile:
        tags_dict = {"tagnames": tags_dict}
        json.dump(tags_dict, tagsfile, ensure_ascii=False, indent=4, separators=(',', ': '))

        # Add a newline character after each item in the JSON output
        tagsfile.write('\n')

def init_delete(file_path):

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"File {file_path} does not exist in the current directory.")


def main():
    directory = '.'  # replace with the path to your directory if necessary
    init_delete(tagnames_file_path)
    init_delete(json_file_path)

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            open_csv_file(filename)
    print("Generated two JSON files")


if __name__ == '__main__':
    main()
