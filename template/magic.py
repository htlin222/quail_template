#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: gen_html_pair
# date: "2023-05-06"
import csv
import json
import os
import re
import shutil
from datetime import datetime

import markdown

json_file_path = "index.json"
tagnames_file_path = "tagnames.json"
cwd = os.getcwd()
folder_name = os.path.basename(cwd)
# ASCII escape sequences for color
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Old file {GREEN}'{filename}'{RESET} has been deleted. ❌ ")
    else:
        print(f"File {GREEN}'{filename}'{RESET} does not exist.")


def split_the_main(main_file):
    with open(main_file, "r") as f:
        markdown_text = f.read()

    # Split the file contents into sections based on the second-level heading
    sections = re.split(r"\n##\s+", markdown_text)[1:]
    main_file_name = os.path.splitext(main_file)[0]

    # Iterate over the sections and write each one to a separate file
    completed_files = []  # List to store the completed filenames
    for i, section in enumerate(sections):
        # TODO: filename as markdown name
        filename = f"{folder_name}{str(i+1).zfill(3)}.md"
        # Generate a filename based on the section number
        with open(filename, "w") as f:
            f.write("## " + section.strip())  # Write the section to a file
        split_by_h3(filename)
        os.remove(filename)
        completed_files.append(filename)

    # Print the total number of completed files
    print(f"👉 {GREEN}{len(completed_files)}{RESET} pairs of Q and S generated")


# }}}
# copy the original file and move it to the backup folder {{{
def copy_and_rename_file(source_path, destination_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Extract the filename and extension from the source path
    filename, extension = os.path.splitext(source_path)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")

    # Create the new filename
    new_filename = f"{filename}_ver_{timestamp}{extension}"

    # Construct the destination path
    destination_path = os.path.join(destination_dir, new_filename)

    # Copy the file to the destination directory with the new name
    shutil.copy2(source_path, destination_path)
    print("...Backing up the original file 🎒 ...\nReady for the magic 🧚 ")


# }}}
# for each pair of Question and solution, split by h3 {{{
def split_by_h3(filename):
    with open(filename, "r") as f:
        markdown_text = f.read()

    # Split markdown by heading 3
    fragments = re.split(r"^### ", markdown_text, flags=re.MULTILINE)
    filename_without_ext = os.path.splitext(filename)[0]
    # Convert each fragment to HTML and save to separate files
    # TODO: Don't use folder name, use markdown filename instaed
    for i, fragment in enumerate(fragments[1:], start=1):
        html = markdown.markdown(fragment, output_format="html")
        with open(f"{filename_without_ext}-s.html", "w") as f:
            f.write(html)

    with open(f"{filename_without_ext}-q.html", "w") as f:
        f.write(markdown.markdown(fragments[0], output_format="html"))


# }}}
# process the csv file, to generate index.json {{{
def open_csv_file(csv_file_path):
    # Open the CSV file and read its contents
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Get the header row

        # Store the original header in a dictionary
        tags_dict = {}
        for i in range(len(header) - 1):
            tags_dict[str(i)] = header[i + 1]

        # Create a new header with values "0" and "1"
        new_header = [str(i) for i in range(len(header) - 1)]

        csv_file_name = os.path.splitext(csv_file_path)[0]
        # Convert each row to a dictionary
        data_dict = {}
        for row in csv_reader:
            key = row[0].zfill(3)  # Pad the key with leading zeros
            data_dict[folder_name + key] = {
                new_header[i]: row[i + 1]
                for i in range(len(new_header))
            }

    # Write the resulting dictionary as JSON
    with open(json_file_path, "w", encoding="utf-8") as jsonfile:
        json.dump(data_dict,
                  jsonfile,
                  ensure_ascii=False,
                  indent=4,
                  separators=(",", ": "))

        # Add a newline character after each item in the JSON output
        jsonfile.write("\n")
        print(f"Preview of the {json_file_path}👇:\n")
        print_first_five_lines(json_file_path)
        print("🤙🤙🤙🤙🤙🤙\n")

    # Write the original header as a separate JSON file
    with open(tagnames_file_path, "w", encoding="utf-8") as tagsfile:
        tags_dict = {"tagnames": tags_dict}
        json.dump(tags_dict,
                  tagsfile,
                  ensure_ascii=False,
                  indent=4,
                  separators=(",", ": "))

        # Add a newline character after each item in the JSON output
        tagsfile.write("\n")


# }}}
# add line breaks to images to avoid text and image in the same line {{{
def add_line_breaks_to_images(file_path):
    # Read the Markdown file
    with open(file_path, "r") as file:
        text = file.read()

    pattern = r"!\[.*?\]\((.*?)\)"
    # Regular expression pattern to match any pattern ending with .jpg
    # Add line breaks before and after the pattern
    result = re.sub(pattern, r"\n\g<0>\n", text)

    # Write the modified text back to the file
    with open(file_path, "w") as file:
        file.write(result)


# }}}


def delete_heading1_lines(file_path):
    # Read the text file
    with open(file_path, "r") as file:
        text = file.read()

    # Delete all heading 1 lines
    result = re.sub(r"^#\s.*$", "", text, flags=re.MULTILINE)

    # Write the modified text back to the file
    with open(file_path, "w") as file:
        file.write(result)


def add_line_break_to_heading3(file_path):
    # Read the text file
    with open(file_path, "r") as file:
        text = file.read()

    # Add a line break after each heading 3
    result = re.sub(r"^(### .*)$", r"\g<0>\n", text, flags=re.MULTILINE)

    # Write the modified text back to the file
    with open(file_path, "w") as file:
        file.write(result)


def add_line_to_top_of_markdown(file_path):
    # Read the Markdown file

    with open(file_path, "r") as file:
        content = file.read()

    filename = os.path.splitext(os.path.basename(file_path))[0]
    # Prepend the line to the existing content
    updated_content = f"# 內專考古題::{filename}\n{content}"

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.write(updated_content)


def print_first_five_lines(file_path):
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            print(line)
            if i == 4:
                break


def main():
    print("Have you downloaded the images locally? \nStart the process 👟 ⏳ ")
    directory = "."  # replace with the path to your directory PRN
    destination_directory = "./original"
    delete_file("index.json")
    # delete_file("progress.json")
    delete_file("choices.json")
    delete_file("tagnames.json")
    for filename in os.listdir(directory):
        # this loop will find all md in current dir,
        # and take it to generate the q-a pair
        if filename.endswith(".md"):
            copy_and_rename_file(filename, destination_directory)
            add_line_breaks_to_images(filename)
            delete_heading1_lines(filename)
            add_line_to_top_of_markdown(filename)
            add_line_break_to_heading3(filename)
            split_the_main(filename)
            print("Generated All the HTML files 😎 🆒 ")

    # now start to handle the csv file to generate the index and tag
    csv_found = False
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            open_csv_file(filename)
            csv_found = True
            print("Generated two JSON files 📋 📋")
            print(f"{GREEN}Done ✨")
    if not csv_found:
        print(f"{RED}ERROR ⚠️  : no csv file, can't generate index.json")


if __name__ == "__main__":
    main()
