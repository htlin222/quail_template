#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: combine_json
# date: "2023-05-14"

import os
import json

# Function to recursively search for 'index.json' files
def search_index_files(directory):
    index_files = []

    for root, dirs, files in os.walk(directory):
        if 'index.json' in files:
            index_files.append(os.path.join(root, 'index.json'))

    return index_files

# Function to combine JSON data from index files
def combine_json_files(index_files):
    combined_data = []

    for file in index_files:
        with open(file, 'r') as f:
            data = json.load(f)
            combined_data.append(data)

    return combined_data

if __name__ == "__main__":
    # Search for 'index.json' files in subdirectories
    directory = '.'  # Specify the root directory to start the search
    index_files = search_index_files(directory)

    # Sort the index files in descending order
    sorted_index_files = sorted(index_files, key=lambda x: int(os.path.basename(x).split('.')[0]), reverse=True)

    # Combine the JSON data from the sorted index files
    combined_data = combine_json_files(sorted_index_files)

    # Write the combined data to a new JSON file
    with open('index.json', 'w') as f:
        json.dump(combined_data, f, indent=4)
