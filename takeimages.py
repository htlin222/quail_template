#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: takeimages
# date: "2023-05-08"

#Import required dependencies
import fitz
import os
from PIL import Image

#Get list of PDF files in current directory
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

#Loop over PDF files
for file_path in pdf_files:
    #Open PDF file
    pdf_file = fitz.open(file_path)

    #Get the number of pages in PDF file
    page_nums = len(pdf_file)

    #Create directory for saved images if it does not exist
    images_dir = os.path.join(os.path.splitext(file_path)[0] + '_圖片')
    if not os.path.isdir(images_dir):
        os.makedirs(images_dir, exist_ok=True)

    #Create empty list to store images information
    images_list = []

    #Extract all images information from each page
    for page_num in range(page_nums):
        page_content = pdf_file[page_num]
        images_list.extend(page_content.get_images())

    print(f"{os.path.splitext(file_path)[0]}，本文件共{page_num}頁")

    #Raise error if PDF has no images
    if len(images_list)==0:
        raise ValueError(f'No images found in {file_path}')

    #Save all the extracted images
    for i, img in enumerate(images_list, start=1):
        #Extract the image object number
        xref = img[0]
        #Extract image
        base_image = pdf_file.extract_image(xref)
        #Store image bytes
        image_bytes = base_image['image']
        #Store image extension
        image_ext = 'png'
        #Generate image file name
        image_name = f"{os.path.splitext(file_path)[0]}_{i}.{image_ext}"
        #Save image
        with open(os.path.join(images_dir, image_name) , 'wb') as image_file:
            image_file.write(image_bytes)
            image_file.close()
    print(f"共{i}張圖片")
