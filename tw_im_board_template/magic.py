#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: gen_html_pair
# date: "2023-05-06"

import markdown
import re
import os

json_file_path = 'index.json'
tagnames_file_path = 'tagnames.json'
cwd = os.getcwd()
folder_name = os.path.basename(cwd)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File '{filename}' has been deleted.")
    else:
        print("File '{filename}' does not exist in the current directory.")

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


def add_line_breaks_to_images(file_path):
    # Read the Markdown file
    with open(file_path, "r") as file:
        text = file.read()

    pattern = r"!\[.*?\]\((.*?)\)"  # Regular expression pattern to match any pattern ending with .jpg
    # Add line breaks before and after the pattern
    result = re.sub(pattern, r"\n\g<0>\n", text)

    # Write the modified text back to the file
    with open(file_path, "w") as file:
        file.write(result)


def split_by_h3(filename):

    with open(filename, 'r') as f:
        markdown_text = f.read()

    # Split markdown by heading 3
    fragments = re.split(r'^### ', markdown_text, flags=re.MULTILINE)
    filename_without_ext = os.path.splitext(filename)[0]
    # Convert each fragment to HTML and save to separate files
    for i, fragment in enumerate(fragments[1:], start=1):
        html = markdown.markdown(fragment, output_format='html')
        with open(f'{folder_name}{filename_without_ext}-s.html', 'w') as f:
            f.write(html)

    with open(f'{folder_name}{filename_without_ext}-q.html', 'w') as f:
        f.write(markdown.markdown(fragments[0], output_format='html'))

def delete_heading1_lines(file_path):
    # Read the text file
    with open(file_path, "r") as file:
        text = file.read()

    # Delete all heading 1 lines
    result = re.sub(r'^#\s.*$', '', text, flags=re.MULTILINE)

    # Write the modified text back to the file
    with open(file_path, "w") as file:
        file.write(result)


def add_line_break_to_heading3(file_path):
    # Read the text file
    with open(file_path, "r") as file:
        text = file.read()

    # Add a line break after each heading 3
    result = re.sub(r'^(### .*)$', r'\g<0>\n', text, flags=re.MULTILINE)

    # Write the modified text back to the file
    with open(file_path, "w") as file:
        file.write(result)
def add_line_to_top_of_markdown(file_path):
    # Read the Markdown file
    with open(file_path, "r") as file:
        content = file.read()

    # Prepend the line to the existing content
    updated_content = "# Hello\n" + content

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.write(updated_content)

def main():
    directory = '.'  # replace with the path to your directory if necessary
    delete_file("index.json")
    delete_file("progress.json")
    delete_file("choices.json")
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            add_line_breaks_to_images(filename)
            delete_heading1_lines(filename)
            add_line_to_top_of_markdown(filename)
            add_line_break_to_heading3(filename)
            splite_the_main(filename)
    print("Generated All the HTML files")

    # for filename in os.listdir(directory):
    #   if filename.endswith('.csv'):
    #        open_csv_file(filename)

    print('Done')


if __name__ == '__main__':
    main()
