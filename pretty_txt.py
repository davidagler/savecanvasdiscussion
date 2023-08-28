'''The output txt files contains HTML tags. We want to remove these. We will remove HTML tags from each .txt. file in discussion_forum/ and write it to a new .txt file with the same name.
'''

# Set path to discussion_forum folder
from bs4 import BeautifulSoup
import os


def remove_html_tags(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            # Read the contents of the file, parse it using BeautifulSoup, then extract text without HTML tags
            with open(file_path, 'r') as file:
                contents = file.read()
            soup = BeautifulSoup(contents, 'html.parser')
            text_without_tags = soup.get_text()

            # Save the .txt back to the file
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(text_without_tags)
    return
