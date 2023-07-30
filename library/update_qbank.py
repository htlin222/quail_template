import os
import subprocess
import sys


def run_another_script(year):
    folder_path = "../" + year + "/"
    script_path = "magic.py"

    try:
        os.chdir(folder_path)
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")


def create_backup(filename):
    try:
        subprocess.run(["cp", filename, f"{filename}.bak"], check=True)
        print(f"Backup of {filename} created successfully as {filename}.bak.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating the backup: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <argument>")
        print("Since there's no argv, will run all of them, from 102 to 111")
        # year = input("Enter three digits (e.g., 101): ")
        user_input = input("Are you sure you want to proceed? (Y/yes): ")
        if user_input.strip().lower() in ["y", "yes"]:
            for i in range(102, 112):  # 102 to 111
                create_backup("progress.json")
                run_another_script(str(i))
    else:
        year = sys.argv[1]
        create_backup("progress.json")
        run_another_script(year)
