#!/bin/bash
# title: update_the_bank
# date created: "2023-06-22"


source_folder="$HOME/Documents/01_內專"

destination_folder="$HOME/Documents/01_內專/export"

# Iterate through each subdirectory in the source folder
for subdirectory in "$source_folder"/*/; do
    # Extract the subdirectory name
    subdirectory_name=$(basename "$subdirectory")

    # Check if the subdirectory name contains digits only
    if [[ $subdirectory_name =~ ^[0-9]+$ ]]; then
        # Zip the subdirectory
        zip_file="$subdirectory_name.zip"
        zip -r "$zip_file" "$subdirectory_name"

        # Move the zip file to the destination folder
        mv "$zip_file" "$destination_folder"
    fi
done
exit 0


