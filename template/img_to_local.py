#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: img_to_local
# date: "2023-05-11"
import os
import requests
import re

# Define a regular expression pattern to match image links in Markdown
pattern = r'\!\[(.*)\]\((http.*?)\)'

# ANSI escape sequences for color
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Define a function to download an image and save it to disk
def download_image(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return True
    else:
        return False

# Loop over all Markdown files in the current directory
for md_file in os.listdir():
    if md_file.endswith('.md'):
        # Get the base directory for the Markdown file
        base_dir = os.path.abspath(os.path.dirname(md_file))

        # Read the contents of the Markdown file
        with open(md_file, 'r') as f:
            md_content = f.read()

        # Find all remote image links in the Markdown content
        for match in re.finditer(pattern, md_content):
            image_alt_text = match.group(1)
            image_url = match.group(2)

            # Generate a local file path for the image based on its URL
            image_file_name = os.path.basename(image_url)
            image_file_path = os.path.join(base_dir, image_file_name)

            # Download the image if it doesn't already exist in the local directory
            if not os.path.exists(image_file_path):
                if download_image(image_url, image_file_path):
                    print(f'{GREEN}Downloaded image{RESET}: {image_url} -> {image_file_path}')
                else:
                    print(f'{RED}權限沒開無法下載{RESET}: {image_url}')

            # Replace the remote image link with a local image path in the Markdown content
            local_image_path = os.path.relpath(image_file_path, base_dir)
            md_content = md_content.replace(match.group(0), f'![{image_alt_text}]({local_image_path})')

        # Save the updated Markdown content to the original file
        with open(md_file, 'w') as f:
            f.write(md_content)
