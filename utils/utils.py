import json
from datetime import datetime


def get_current_datetime():
    """Get current date and time"""
    now = datetime.now()

    # Format the date-time string
    formatted_datetime = now.strftime("%Y-%m-%d_%H_%M_%S")

    return formatted_datetime


def open_md(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    return md_content


def open_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        json_meta = json.load(f)
    return json_meta