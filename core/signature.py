from pathlib import Path

# --- FORENSIC GLOBAL CONFIGURATIONS ---
HEADER_SIZE = 8

SIGNATURES = {
    b"%PDF": "PDF Document",
    b"\x89PNG": "PNG Image",
    b"\xFF\xD8\xFF": "JPEG Image",
    b"PK\x03\x04": "ZIP Archive",
    b"MZ": "Windows Executable"
}

# Maps detected signature types to their standard extension variations
EXPECTED_EXTENSIONS = {
    "PDF Document": [".pdf"],
    "PNG Image": [".png"],
    "JPEG Image": [".jpg", ".jpeg"],
    "ZIP Archive": [".zip"],
    "Windows Executable": [".exe", ".dll"]
}

def verify_signature(file_path: str) -> dict:
    # Step 2: Validation
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
        
    if not path.is_file():
        raise IsADirectoryError(f"{file_path} is not a file.")
        
    # Step 3: Read Hex Header (Using HEADER_SIZE constant)
    with path.open("rb") as file:
        header = file.read(HEADER_SIZE)
        
    # Standardized hexadecimal presentation for the investigator
    magic_bytes_hex = header.hex().upper()
    file_extension = path.suffix.lower()
    
    # Step 5: Comparison Engine
    for signature, file_type in SIGNATURES.items():
        if header.startswith(signature):
            # Step 2 (Improvement): Integrity Check Validation
            allowed_extensions = EXPECTED_EXTENSIONS.get(file_type, [])
            
            if file_extension in allowed_extensions:
                status = "Valid"
            else:
                status = "Suspicious"  # Triggers if a signature mismatches its extension
                
            return {
                "File Name": path.name,
                "Extension": path.suffix,
                "Detected Type": file_type,
                "Magic Bytes": magic_bytes_hex,
                "Status": status
            }
            
    # Fallback return for unrecognized signatures
    return {
        "File Name": path.name,
        "Extension": path.suffix,
        "Detected Type": "Unknown",
        "Magic Bytes": magic_bytes_hex,
        "Status": "Unknown Signature"
    }