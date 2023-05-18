#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: md_to_anki
# date: "2023-05-18"
import os
import subprocess
import sys

def modify_markdown_file(file):
    # Read the content of the markdown file
    with open(file, "r") as f:
        content = f.readlines()

    # Modify the content by adding '%' before heading level 3
    modified_content = []
    for line in content:
        if line.startswith("###"):
            modified_content.append("%\n" + line)
        else:
            modified_content.append(line)

    # Create the new filename for Anki
    new_filename = file.replace(".md", "_for_anki.md")

    # Write the modified content to the new file
    with open(new_filename, "w") as f:
        f.writelines(modified_content)

    # Run the subprocess to generate the Anki package
    subprocess.run(["mdanki", new_filename, file.replace(".md", ".apkg")], capture_output=True, text=True)

    print(f"Anki package '{file.replace('.md', '.apkg')}' created successfully.")

    # Delete the modified markdown file
    # os.remove(new_filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python markdown_to_anki.py <markdown_file>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    if not os.path.isfile(markdown_file):
        print(f"Error: {markdown_file} does not exist or is not a file.")
        sys.exit(1)

    modify_markdown_file(markdown_file)
