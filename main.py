import json
from helpers import *
from csv_creation import *
from txt_creation import *
from folder_creation import create_folder
import constants as c
from pretty_txt import remove_html_tags

def run():
    # Prompt the user to enter the JSON file path
    json_file_path = input("Enter the path to the JSON file: ")

    # Read the JSON file and load its contents into a variable
    with open(json_file_path, encoding="utf-8") as file:
        data = json.load(file)

    # Call the helper functions
    student_names_ids = get_student_names_ids(data)
    studentids_messages = get_studentids_messages(data)
    student_id_replies = get_student_id_replies(data)
    combined_data = combine_data(student_names_ids, studentids_messages, student_id_replies)

    #Pass combined_data to create_csv function
    create_csv(combined_data)

    # Create a folder for txt files
    txt_folder_name = c.OUT_TXT
    create_folder(txt_folder_name)

    #Pass csv_file to create_student_files function
    create_student_files(csv_file)

    # Remove HTML from txt files
    remove_html_tags(txt_folder_name)

if __name__ == "__main__":
    run()