#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: reset_number
# date: "2023-05-26"

import re

# Define the input and output file paths
input_file = "input.md"
output_file = "output.md"

# Define the pattern to match
pattern = r"## Question (\d+)"

# Define the starting and ending numbers
start_number = 1
end_number = 10
diff = 2

# Read the input file line by line and write modified lines to the output file
with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    for line in file_in:
        match = re.search(pattern, line)
        if match:
            question_number = int(match.group(1))
            if start_number <= question_number <= end_number:
                modified_number = question_number + diff
                modified_line = line.replace(str(question_number), str(modified_number))
                file_out.write(modified_line)
            else:
                file_out.write(line)
        else:
            file_out.write(line)
