'''CSV file that writes the combined_data dictionary to a CSV file. '''
import csv
import constants as c


def create_csv(combined_data):
    # Get the maximum number of replies for any student
    max_replies = max(len(combined_data[student]["replies"]) for student in combined_data)

    # Prepare the column headers
    headers = ["student_name", "initial_post"]
    headers.extend([f"reply_{i+1}" for i in range(max_replies)])

    # Prepare the rows for writing to the CSV
    rows = []
    for student_name, student_data in combined_data.items():
        row = [student_name, student_data["initial_post"]]
        if student_data["replies"]: # Check replies exist
            row.extend(student_data["replies"])
        else:
            row.extend([""] * max_replies)  # Empty strings for missing replies
        rows.append(row)
    with open(c.csv_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    return


