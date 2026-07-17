from core.hashing import calculate_hash
from core.ioc import scan_iocs
from core.metadata import analyze_metadata
from core.signature import verify_signature

# Global Constants
ALGORITHMS = {"1": "md5", "2": "sha1", "3": "sha256", "4": "sha512"}


# 1. Banner Function
def print_banner():
    print("=" * 55)
    print("              DFIR Toolkit v1.0")
    print("   Digital Forensics & Incident Response")
    print("=" * 55)


# 2. Menu Display
def display_menu():
    print("\n====== DFIR Toolkit Menu ======")
    print("1. Hash Calculator")
    print("2. Metadata Analysis")
    print("3. File Signature Verification")
    print("4. IOC Scanner")
    print("5. Exit")
    print("===============================")


# 3. Wrapper Functions for Core Logic
def run_hash():
    print("\n--- Hash Calculator ---")
    file_path = input("Enter the path of the file to hash: ").strip()

    print("\nAvailable Algorithms:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    print("4. SHA-512")
    algo_choice = input("Select an algorithm (1-4): ").strip()

    if algo_choice not in ALGORITHMS:
        print("[-] Error: Invalid algorithm selection.")
        input("\nPress Enter to return to the main menu...")
        return

    selected_algo = ALGORITHMS[algo_choice]

    try:
        hash_value = calculate_hash(file_path, selected_algo)

        # Cleaner, professional block layout
        print("\n" + "=" * 55)
        print("Hash Result")
        print("=" * 55)
        print(f"Algorithm           : {selected_algo.upper()}")
        print(f"Hash                : {hash_value}")
        print("=" * 55)

    except FileNotFoundError:
        print(f"[-] Error: The file '{file_path}' could not be found.")
    except IsADirectoryError:
        print(f"[-] Error: '{file_path}' is a directory.")
    except PermissionError:
        print(f"[-] Error: Permission denied for '{file_path}'.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

    input("\nPress Enter to return to the main menu...")


def run_metadata():
    print("\n--- Metadata Analysis ---")
    file_path = input("Enter the path of the file to analyze: ").strip()
    try:
        metadata = analyze_metadata(file_path)

        print("\n[+] Metadata Extracted:")
        # Left-aligned keys for an even layout
        for key, value in metadata.items():
            print(f"  {key:<20}: {value}")

    except FileNotFoundError:
        print(f"[-] Error: The file '{file_path}' could not be found.")
    except IsADirectoryError:
        print(f"[-] Error: '{file_path}' is a directory.")
    except PermissionError:
        print(f"[-] Error: Permission denied for '{file_path}'.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

    input("\nPress Enter to return to the main menu...")


def run_signature():
    print("\n--- File Signature Verification ---")
    file_path = input("Enter the path of the file to verify: ").strip()
    try:
        result = verify_signature(file_path)

        print("\n[+] Signature Analysis Results:")
        # Left-aligned keys for symmetry matching metadata
        for key, value in result.items():
            print(f"  {key:<20}: {value}")

    except FileNotFoundError:
        print(f"[-] Error: The file '{file_path}' could not be found.")
    except IsADirectoryError:
        print(f"[-] Error: '{file_path}' is a directory.")
    except PermissionError:
        print(f"[-] Error: Permission denied for '{file_path}'.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

    input("\nPress Enter to return to the main menu...")


def run_ioc():
    print("\n--- Indicators of Compromise (IOC) Scanner ---")
    file_path = input("Enter the path of the file to scan: ").strip()

    try:
        results = scan_iocs(file_path)

        print("\n" + "=" * 55)
        print("IOC Scan Report")
        print("=" * 55)
        print(f"Total Emails Found  : {results['Total Emails']}")
        print(f"Total IPs Found     : {results['Total IPs']}")
        print(f"Total URLs Found    : {results['Total URLs']}")
        print("=" * 55)

        if results["Emails"]:
            print("\n--- Detected Emails ---")
            for email in results["Emails"]:
                print(f"  - {email}")

        if results["IP Addresses"]:
            print("\n--- Detected IP Addresses ---")
            for ip in results["IP Addresses"]:
                print(f"  - {ip}")

        if results["URLs"]:
            print("\n--- Detected URLs ---")
            for url in results["URLs"]:
                print(f"  - {url}")

        if (
            not results["Emails"]
            and not results["IP Addresses"]
            and not results["URLs"]
        ):
            print("\n[!] No Indicators of Compromise detected.")

    except FileNotFoundError:
        print(f"[-] Error: The file '{file_path}' could not be found.")
    except IsADirectoryError:
        print(f"[-] Error: '{file_path}' is a directory, not a file.")
    except PermissionError:
        print(f"[-] Error: Permission denied to read '{file_path}'.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

    input("\nPress Enter to return to the main menu...")


# 4. Main Control Loop
def main():
    print_banner()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            run_hash()
        elif choice == "2":
            run_metadata()
        elif choice == "3":
            run_signature()
        elif choice == "4":
            run_ioc()
        elif choice == "5":
            print("\nThank you for using DFIR Toolkit.")
            break
        else:
            print(
                "\n[-] Invalid choice. Please select a valid option between 1 and 5."
            )


if __name__ == "__main__":
    main()