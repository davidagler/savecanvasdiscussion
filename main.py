import json
from helpers import *
from csv_creation import *
from txt_creation import *
from folder_creation import create_folder
import constants as c
from pretty_txt import remove_html_tags


# Check encoding
import chardet




def run():
    # Prompt the user to enter the JSON file path
    json_file_path_input = input("Enter the path to the JSON file: ")
    json_file_path = json_file_path_input.replace("/", "\\")

    # Detect the encoding of the file
    with open(json_file_path, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']

    try:
        # Read the JSON file and load its contents into a variable
        with open(json_file_path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return
    except Exception as e:
        print(f"Error occurred while reading the JSON file: {e}")
        return

    # Call the helper functions
    student_names_ids = get_student_names_ids(data)
    studentids_messages = get_studentids_messages(data)
    student_id_replies = get_student_id_replies(data)
    combined_data = combine_data(student_names_ids, studentids_messages, student_id_replies)
    # Pass combined_data to create_csv function
    create_csv(combined_data)

    # Create a folder for txt files
    txt_folder_name = c.OUT_TXT
    create_folder(txt_folder_name)
    print(f"Created a folder named {txt_folder_name} in the current directory.")

    # Pass csv_file to create_student_files function
    create_student_files(c.csv_file)
    print(f"Created txt files for each student in the {txt_folder_name} folder.")

    # Remove HTML from txt files
    remove_html_tags(txt_folder_name)
    print(f"Cleaned up HTML from each txt file.")


if __name__ == "__main__":
    run()
