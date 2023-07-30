import os
import sys


def copy_file(filename, output_folder):
    # Define the paths to the source and destination files
    source_file_path = os.path.join(".", output_folder, f"{filename}.md")
    destination_file_path = os.path.join("..", f"{filename}", f"{filename}.md")

    # Check if the source file exists
    if os.path.exists(source_file_path):
        # Read the contents of the source file
        with open(source_file_path, "r") as source_file:
            file_contents = source_file.read()

        # Create the destination directory if it doesn't exist
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

        # Write the contents to the destination file
        with open(destination_file_path, "w") as destination_file:
            destination_file.write(file_contents)

        print(
            f"👌 File '{filename}.md' has been copied to '../{filename}/{filename}.md'"
        )
    else:
        print(f"Source file '{filename}.md' does not exist in './output/'")


def create_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")


def combine_files(user_input, output_folder):
    output_filename = f"{output_folder}/{user_input}.md"
    with open(output_filename, "w") as output_file:
        # Adding the title at the first line
        output_file.write(f"# 內專 {user_input} 考古題\n\n")
        for filename in sorted(os.listdir(".")):
            if (filename.endswith(".md") and filename[:6].isdigit()
                    and filename[:3] == user_input):
                with open(filename, "r") as input_file:
                    content = input_file.read()
                    output_file.write(content)
                    # Adding a line break between files
                    output_file.write("\n")

    delete_brackets(output_filename)

    print(
        f"\n🎉 All questions of {user_input} have been combined into {user_input}.md in folder './{output_folder}'"
    )


def delete_brackets(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Remove all occurrences of [[ and ]]
    content = content.replace("[[", "").replace("]]", "")

    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    output_folder = "output"
    create_output_folder()
    # manually input one year
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <argument>")
        print("Since there's no argv, will run all of them, from 102 to 111")
        # year = input("Enter three digits (e.g., 101): ")
        user_input = input("Are you sure you want to proceed? (Y/yes): ")
        if user_input.strip().lower() in ["y", "yes"]:
            for i in range(102, 112):  # 102 to 111
                combine_files(str(i), output_folder)
                copy_file(str(i), output_folder)
    else:
        year = sys.argv[1]
        combine_files(year, output_folder)
        copy_file(year, output_folder)
    # END
