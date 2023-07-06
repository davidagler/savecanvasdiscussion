def get_student_names_ids(data):
    """Returns a dictionary of student names and IDs from the input JSON data."""
    users = data["participants"]
    student_names_ids = {}
    for user in users:
        display_name = user["display_name"]
        participant_id = user["id"]
        student_names_ids[display_name] = participant_id

    return student_names_ids

def get_studentids_messages(data):
    """Returns a dictionary of student IDs and their initial posts from the input JSON data."""
    posts = data["view"]
    studentids_messages = {}
    for post in posts:
        user_id = post["user_id"]
        message = post["message"]
        studentids_messages[user_id] = message

    return studentids_messages

def get_student_id_replies(data):
    """Returns a dictionary of student IDs and their replies from the input JSON data."""
    posts = data["view"]
    student_id_replies = {}
    for post in posts:
        user_id = post["user_id"]
        replies = post.get("replies", [])
        for reply in replies:
            reply_user_id = reply["user_id"]
            reply_message = reply["message"]
            if reply_user_id not in student_id_replies:
                student_id_replies[reply_user_id] = []
            student_id_replies[reply_user_id].append(reply_message)

    return student_id_replies

def combine_data(student_names_ids, studentids_messages, student_id_replies):
    """Returns a dictionary of student names, IDs, initial posts, and replies."""
    combined_data = {}
    for student_name, student_id in student_names_ids.items():
        if student_id in studentids_messages and student_id in student_id_replies:
            initial_post = studentids_messages[student_id]
            replies = student_id_replies[student_id]
            combined_data[student_name] = {"initial_post": initial_post, "replies": replies}

    return combined_data

