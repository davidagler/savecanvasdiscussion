import csv
import os
import constants as c

# Creates a folder at the specified path

def create_student_files(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        # Loop through looking for the student's name
        for row in reader:
            student_name = row[0]
            discussion_post = row[1]

            # Create a text file for each student
            file_path = os.path.join(c.OUT_TXT, f"canvas_dis_{student_name}.txt")
            with open(file_path, "w") as txtfile:
                txtfile.write(f"STUDENT NAME: {student_name}\n")
                txtfile.write(f"\n{discussion_post}\n")
                txtfile.write(f"******************************\n")

                # Iterate over the replies dynamically based on the number of columns
                for i in range(2, len(row)):
                    reply = row[i]
                    reply_number = i - 1
                    txtfile.write(f"Reply {reply_number}: {reply}\n")
                    txtfile.write(f"******************************\n")

                # Handle the case when there are no further replies
                if len(row) <= 2:
                    txtfile.write("No Further Replies\n")
                    txtfile.write(f"******************************\n")
