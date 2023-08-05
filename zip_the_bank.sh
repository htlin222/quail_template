#!/bin/bash
# title: update_the_bank
# date created: "2023-06-22"

source_folder="./"
destination_folder="./export"

if [ ! -d "$destination_folder" ]; then
    mkdir "$destination_folder"
fi

# Iterate through each subdirectory in the source folder
for subdirectory in "$source_folder"/*/; do
    # Extract the subdirectory name
    subdirectory_name=$(basename "$subdirectory")

    # Check if the subdirectory name contains digits only
    if [[ $subdirectory_name =~ ^[0-9]+$ ]]; then
        # Check if the "progress.json" file exists in the subdirectory
        progress_file="$subdirectory/progress.json"
        # if [ -f "$progress_file" ]; then
        #     echo "Skipping '$subdirectory_name' due to 'progress.json' file presence."
        #     continue
        # fi

        # Zip the subdirectory (excluding "progress.json" file)
        zip_file="$subdirectory_name.zip"
        cd "$source_folder"
        zip -r "$destination_folder/$zip_file" "$subdirectory_name" -x "$subdirectory_name/progress.json"
    fi
done
exit 0
