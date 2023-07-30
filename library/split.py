# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# title: split_by_heading
# date created: "2023-01-23"
import argparse
import os
import re
import sys
from datetime import datetime

current_date_time = datetime.now()
string_date_time = current_date_time.strftime("%Y-%m-%d")


def replace_h2_with_number(file_path):
    # Read the content of the markdown file
    with open(file_path, "r") as file:
        content = file.read()

    # Regular expression to find h2 headings (## title...)
    h2_pattern = r"^##\s(.+)$"

    # Function to replace matched h2 headings with numbered titles
    def replace_heading(match):
        nonlocal counter
        counter += 1
        return f"## {counter:03d}"

    # Initialize the counter for numbering
    counter = 0

    # Use re.sub to replace each matched h2 heading with a numbered title
    updated_content = re.sub(h2_pattern,
                             replace_heading,
                             content,
                             flags=re.MULTILINE)

    # Write the updated content back to the markdown file
    with open(file_path, "w") as file:
        file.write(updated_content)


def main(file_path, heading_level):
    """
    Split markdown by heading level.
    """
    heading_list = ["NONE", "# ", "## ", "### ", "#### ", "##### ", "###### "]
    level = heading_list[int(heading_level)]
    higher_level_list = heading_list[1:int(heading_level)]
    with open(file_path, "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith(level):
                mother_name = os.path.basename(file_path)[:-3]
                strip_level = int(heading_level) + 1
                heading = lines[i].strip()[strip_level:]
                split_filename = heading + ".md"
                wikilink = "[[" + mother_name + heading + "]] 第 " + heading + " 題"
                child_name = mother_name + split_filename
                print(child_name)
                lines[i] = lines[i].replace(heading, wikilink)
                lines[i] = lines[i].replace(level, "- ")
                context = re.sub(r"\n", " ", lines[i + 2][:60])
                lines[i] = lines[i] + "  - [ ] " + context + "...\n"
                with open(child_name, "a") as f:
                    new_front_and_heading = ("## 第 " + heading + " 題 - 內專 [[" +
                                             mother_name + "]] 年\n")
                    f.write(new_front_and_heading)
                    i += 1
                    while (i < len(lines) and not lines[i].startswith(level)
                           and all(not lines[i].startswith(string)
                                   for string in higher_level_list)):
                        f.write(lines[i])
                        lines[i] = ""
                        i += 1
                    #
                numerical_value = int(heading)
                lines_to_append = [
                    "\n---\n\n",
                    "- 上一題: [[{}{:03d}]]\n".format(mother_name,
                                                   numerical_value - 1),
                    "- 下一題: [[{}{:03d}]]\n".format(mother_name,
                                                   numerical_value + 1),
                ]
                with open(child_name, "a") as file:
                    file.writelines(lines_to_append)
            else:
                i += 1
    with open(file_path, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--level",
    #                     type=int,
    #                     help="level of heading",
    #                     default=2)
    # parser.add_argument("--file", type=str, help="file name")
    # args = parser.parse_args()
    #
    # if not os.path.exists(args.file):
    #     print(f"Error: file '{args.file}' does not exist")
    #     sys.exit(1)
    # heading_level = args.level
    # one file
    # original_file = args.file
    # current_directory = os.getcwd()
    # file_path = os.path.join(current_directory, original_file)
    # replace_h2_with_number(file_path)
    # main(file_path, heading_level)
    # batch
    for i in range(102, 112):  # 102 to 111
        original_file = str(i) + ".md"
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, original_file)
        replace_h2_with_number(file_path)
        main(file_path, 2)
