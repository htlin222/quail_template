#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: topdf
# date: "2023-06-21"

# author: Hsieh-Ting Lin, the Lizard 🦎
# {{{ import here 👉 # }}}
import os
import subprocess
# }}}

def remove_content_and_images(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    current_heading_level = 0
    skip_lines = False

    for line in lines:
        if line.startswith('#'):
            heading_level = line.count('#')
            if heading_level == 3:
                current_heading_level = 3
                skip_lines = True
            elif heading_level > 3:
                current_heading_level = heading_level
            else:
                current_heading_level = 0
                skip_lines = False

        if not skip_lines and not line.startswith('!['):
            modified_lines.append(line)

    return modified_lines

def save_modified_markdown(file_path, modified_lines):
    new_file_path = file_path.replace('.md', '_no_answer.md')
    with open(new_file_path, 'w') as file:
        file.writelines(modified_lines)
    return new_file_path

def process_markdown_files(folder_path):
    files = [file for file in os.listdir(folder_path) if file.endswith('.md')]
    for file in files:
        file_path = os.path.join(folder_path, file)
        modified_lines = remove_content_and_images(file_path)
        new_file_path = save_modified_markdown(file_path, modified_lines)
        output_file_path = new_file_path.replace('.md', '.docx')
        subprocess.run(['pandoc', '-o', output_file_path, '-f', 'markdown', '-t', 'docx', '--reference-doc=ref.docx', new_file_path])
        os.remove(new_file_path)

# Provide the path to the folder containing the Markdown files
folder_path = '.'

process_markdown_files(folder_path)
