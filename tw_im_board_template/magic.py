#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: gen_html_pair
# date: "2023-05-06"

import markdown
import re
import os


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


def main():
    directory = '.'  # replace with the path to your directory if necessary
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            splite_the_main(filename)

    print('Done')


if __name__ == '__main__':
    main()
