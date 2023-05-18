#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: pdftomd
# date: "2023-05-08"

import os
import pdfplumber

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.join(directory, filename)
        with pdfplumber.open(filepath) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
                print(text)
        # Save the extracted text as a markdown file
        md_filename = os.path.splitext(filename)[0] + '_未處理.md'
        with open(md_filename, 'w') as f:
            f.write(text)
