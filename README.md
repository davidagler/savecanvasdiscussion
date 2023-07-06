# Save CANVAS Discussion as CSV and TXT Files

This script will save a Canvas discussion as a CSV file and TXT files. The CSV file will contain the the student name (their display name correlated to their user id), their discussion post, and then replies by the student. The script saves the same information but in individual .txt files, one for each student.

## Getting Started

You'll need the JSON file from Canvas that contains the discussion information. You can get this by going to the discussion in Canvas, 

https://{school_abbreviation}.instructure.com/api/v1/courses/{course_id}/discussion_topics/{more_data}/view?include_new_entries=1&include_enrollment_state=1

Next, you'll want to know the file path of the JSON file. You can do this by right clicking on the file and selecting "Properties". Copy the file path. When you run the script, you'll paste the file path into the command line. The script will take care of the rest. 