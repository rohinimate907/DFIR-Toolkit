from datetime import datetime
from pathlib import Path


def generate_timeline(folder_path: str) -> list:
    path = Path(folder_path)

    # Step 1 — Validation
    if not path.exists():
        raise FileNotFoundError(
            f"The directory at '{folder_path}' does not exist."
        )

    if not path.is_dir():
        raise NotADirectoryError(f"The path '{folder_path}' is not a directory.")

    timeline = []

    # Steps 2 to 5 — Folder Scanning & Data Collection
    for item in path.iterdir():
        if not item.is_file():
            continue

        stats = item.stat()

        event = {
            "File Name": item.name,
            "Created": datetime.fromtimestamp(stats.st_ctime),
            "Modified": datetime.fromtimestamp(stats.st_mtime),
            "Accessed": datetime.fromtimestamp(stats.st_atime),
        }
        timeline.append(event)

    # Step 6 — Sorting (Oldest to Newest based on Creation Time)
    timeline.sort(key=lambda event: event["Created"])

    # Step 7 — Format Time (Converting datetime objects to clean strings)
    for event in timeline:
        event["Created"] = event["Created"].strftime("%Y-%m-%d %H:%M:%S")
        event["Modified"] = event["Modified"].strftime("%Y-%m-%d %H:%M:%S")
        event["Accessed"] = event["Accessed"].strftime("%Y-%m-%d %H:%M:%S")

    return timeline