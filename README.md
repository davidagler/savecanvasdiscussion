# Save CANVAS Discussion as CSV and TXT Files

This script will save a Canvas discussion as a CSV file and TXT files. The CSV file will contain the the student name (their display name correlated to their user id), their discussion post, and then replies by the student. The script saves the same information but in individual .txt files, one for each student.

## Getting Started

You'll need the JSON file from Canvas that contains the discussion information. You can get the .json file by modifying the following link:

```html
https://{school_abbreviation}.instructure.com/api/v1/courses/{course_id}/discussion_topics/{more_data}/view?include_new_entries=1&include_enrollment_state=1
```

The {school_abbreviation} is the abbreviation for your school. You can typically view this abbreviation in a section of your CANVAS course. For example, the abbreviation for The Pennsylvania State University is "psu". The {course_id} is the course id for the section of the course. The {more_data} is the discussion id. You can get this by going to the discussion in Canvas and looking at the URL.

Next, you'll want to know the file path of the JSON file. When you run main.py, it will ask for a file path for the JSON file. Supply the file path and the script will run, creating a CSV file and TXT files.
