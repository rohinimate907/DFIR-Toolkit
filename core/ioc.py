import re
from pathlib import Path


def scan_iocs(file_path: str) -> dict:
    """Scan a text file for common Indicators of Compromise (IOCs).

    Args:
        file_path: Path to the text file.

    Returns:
        Dictionary containing detected IOCs.
    """

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    if not path.is_file():
        raise IsADirectoryError(
            f"The path {file_path} is a directory, not a file."
        )

    with path.open("r", encoding="utf-8", errors="ignore") as file:
        content = file.read()

    EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    IP_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    URL_PATTERN = r"https?://[^\s]+"

    emails = re.findall(EMAIL_PATTERN, content)
    ip_addresses = re.findall(IP_PATTERN, content)
    urls = re.findall(URL_PATTERN, content)

    # De-duplicate and sort (Ab ye functions proper function ke andar indented hain)
    emails = sorted(set(emails))
    ip_addresses = sorted(set(ip_addresses))
    urls = sorted(set(urls))

    return {
        "Emails": emails,
        "IP Addresses": ip_addresses,
        "URLs": urls,
        "Total Emails": len(emails),
        "Total IPs": len(ip_addresses),
        "Total URLs": len(urls),
    }