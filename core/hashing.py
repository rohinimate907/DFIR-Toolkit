import hashlib
from pathlib import Path


def calculate_hash(file_path: str, algorithm: str) -> str:
    """
    Calculate the cryptographic hash of a file.

    Args:
        file_path: Path to the target file.
        algorithm: Hash algorithm (md5, sha1, sha256, sha512).

    Returns:
        Hexadecimal hash string.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError("The given path is not a file.")

    algorithm = algorithm.lower()

    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hash_object = hashlib.new(algorithm)

    with open(path, "rb") as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)

    return hash_object.hexdigest()