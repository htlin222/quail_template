#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: gen_html_pair
# date: "2023-05-06"

import markdown
import re
import csv
import json
import os

json_file_path = 'index.json'
tagnames_file_path = 'tagnames.json'

def splite_the_main(main_file):

    with open(main_file, 'r') as f:
        markdown_text = f.read()

    # Split the file contents into sections based on the second-level heading
    sections = re.split(r'\n##\s+', markdown_text)[1:]

    # Iterate over the sections and write each one to a separate file
    for i, section in enumerate(sections):
        filename = f'{str(i+1).zfill(3)}.md'
        # Generate a filename based on the section number
        with open(filename, 'w') as f:
            f.write('## ' + section.strip())  # Write the section to a file
        split_by_h3(filename)
        os.remove(filename)
        print(f"{filename} completed.")


def split_by_h3(filename):

    with open(filename, 'r') as f:
        markdown_text = f.read()

    # Split markdown by heading 3
    fragments = re.split(r'^### ', markdown_text, flags=re.MULTILINE)
    filename_without_ext = os.path.splitext(filename)[0]
    # Convert each fragment to HTML and save to separate files
    for i, fragment in enumerate(fragments[1:], start=1):
        html = markdown.markdown(fragment, output_format='html')
        with open(f'{filename_without_ext}-s.html', 'w') as f:
            f.write(html)

    with open(f'{filename_without_ext}-q.html', 'w') as f:
        f.write(markdown.markdown(fragments[0], output_format='html'))


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
        new_header = ["0", "1"]

        # Convert each row to a dictionary
        data_dict = {}
        for row in csv_reader:
            key = row[0].zfill(3)  # Pad the key with leading zeros
            data_dict[key] = {new_header[i]: row[i+1] for i in range(len(new_header))}

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
    print("Generated two JSON files")


def main():
    directory = '.'  # replace with the path to your directory if necessary
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            splite_the_main(filename)
    print("Generated All the HTML files")

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            open_csv_file(filename)

    print('Done')


if __name__ == '__main__':
    main()
