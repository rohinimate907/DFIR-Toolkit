from pathlib import Path
from datetime import datetime

def format_file_size(size: int) -> str:
    """Convert bytes to a human-readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def analyze_metadata(file_path: str) -> dict:
    # STEP 1 — Create Path Object
    path = Path(file_path)
    
    # STEP 2 — Validation
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
        
    if not path.is_file():
        raise IsADirectoryError(f"{file_path} is not a file.")
        
    # STEP 3 — File Statistics
    stats = path.stat()
    
    # STEP 4 — Time Parsing (Cleaned up to avoid repetition)
    created_time = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
    modified_time = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    accessed_time = datetime.fromtimestamp(stats.st_atime).strftime("%Y-%m-%d %H:%M:%S")
    
    # STEP 5 — Metadata Dictionary Generation
    metadata = {
        "File Name": path.name,
        "Extension": path.suffix,
        "Absolute Path": str(path.resolve()),
        "Parent Folder": str(path.parent),
        "File Size": format_file_size(stats.st_size),
        "Bytes": stats.st_size,
        "Created": created_time,
        "Modified": modified_time,
        "Accessed": accessed_time,
    }
    
    # STEP 6 — Return
    return metadata