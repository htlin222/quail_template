#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: create_apkg
# date: "2023-05-18"
import sys
import os
import re
import subprocess
import shutil
import glob


def replace_markdown(text):
    text = re.sub(r'^##\s', r'<div data-question markdown="block">\n\n## ', text, flags=re.MULTILINE)
    text = re.sub(r'^###\s', r'</div>\n### ', text, flags=re.MULTILINE)
    return text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        file_dir, file_name = os.path.split(file_path)
        output_dir = "output_for_anki"
        input_dir = "input_for_anki"
        output_path = os.path.join(output_dir, file_name)
        input_path = os.path.join(input_dir, file_name)

        # Create input_for_anki directory if it doesn't exist
        os.makedirs(input_dir, exist_ok=True)

        with open(file_path, 'r') as file:
            markdown_text = file.read()
            modified_text = replace_markdown(markdown_text)

        with open(input_path, 'w') as file:
            file.write(modified_text)
            print(f"Modified Markdown file has been saved to {input_path}")

        # Copy images to input_for_anki directory
        image_extensions = ['.jpg', '.png', '.jpeg']
        image_files = [f for ext in image_extensions for f in glob.glob(f"*{ext}")]
        for image_file in image_files:
            shutil.copy(image_file, input_dir)

        # Create output_for_anki directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Check if mdankideck is installed, and if not, install it
        try:
            subprocess.run(['mdankideck', '--version'], check=True)
        except FileNotFoundError:
            print("mdankideck not found. Installing markdown-anki-decks package...")
            subprocess.run(['pip', 'install', 'markdown-anki-decks'])

        # Run mdankideck subprocess
        subprocess.run(['mdankideck', input_dir, output_dir])
        print(f"mdankideck process completed. Output files are saved in {output_dir}")

        # Delete input_for_anki folder
        shutil.rmtree(input_dir)
        print(f"input_for_anki folder has been deleted.")
    else:
        print("Please provide a Markdown file as a command-line argument.")
