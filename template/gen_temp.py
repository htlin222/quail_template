#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: gen_temp
# date: "2023-05-06"
import os

current_dir = os.getcwd()
folder_name = os.path.basename(current_dir)
markdown_name = folder_name + ".md"
csv_name = folder_name + ".csv"
print(f"In {folder_name}, \ncreate {folder_name}.md and {folder_name}.csv")


def get_valid_number():
    while True:
        try:
            number = int(
                input(
                    "How many question do you want? Please enter a number less than 1000: "
                ))
            if number >= 1000:
                print("Error: Number must be less than 1000.")
            else:
                return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


number = get_valid_number() + 1
with open(markdown_name, "w") as f:
    f.write(f"# 範列檔案::{folder_name}\n\n")
    for i in range(1, number):
        text = f"""## Question {i}:

題幹

![圖片放這](https://i.imgur.com/dqopYB9b.jpg)

---

- A.
- B.
- C.
- D.
- E.

### Correct Answer: A

上面要空一行，然後接著詳解如下…

"""
        f.write(text)

with open(csv_name, "w") as f:
    f.write("題號,次專,考古_是1_否0,年份\n")
    for i in range(1, number):
        padded_i = str(i).zfill(3)
        text = f"{i},科科科,0,{folder_name}\n"
        f.write(text)

print("Done ✨")
