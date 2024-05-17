import os  # Imports `os` module for file system operations
from datetime import datetime  # Imports `datetime` class for date/time manipulation

def compare_and_flag_files(error_log_file, folder_path):
    """
    Compares XML references in an error log with a folder, flags missing files,
    and saves them to separate text files named with timestamps.
    
    """

    # Get current timestamp for filenames (YYYY-MM-DD_HH-MM-SS format)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Construct filenames with timestamp (e.g., missing_files_2024-05-17_16-15-00.txt)
    missing_file_log = f"missing_files_{timestamp}.txt"
    matched_file_log = f"matched_files_{timestamp}.txt"

    # Get folder filenames as a set (efficient for lookups in large folders)
    folder_files = set(os.listdir(folder_path))

    # Open files for writing with context manager (automatic closing)
    with open(missing_file_log, 'w') as missing_file, open(matched_file_log, 'w') as matched_file:
        # Open error log file for reading with context manager
        with open(error_log_file, 'r') as error_log:
            for line in error_log:
                # Extract referenced XML filename (assuming filename only, no path)
                xml_filename = line.strip().split('/')[-1]

                # Check if file exists in folder using membership in set
                if xml_filename in folder_files:
                    # File found, write to matched file
                    matched_file.write(f"Matched file: {xml_filename}\n")
                else:
                    # File not found, write to missing file
                    missing_file.write(f"Missing file: {xml_filename}\n")


if __name__ == "__main__":
    # Get user input for file paths (directory and folder name)
    error_log_dir = input("Enter the directory containing the error log file: ")
    folder_name = input("Enter the name of the folder containing the XML files: ")

    # Construct full paths based on user input and current working directory
    error_log_file = os.path.join(error_log_dir, "error_log.txt")  # Assuming "error_log.txt" as filename
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Call the function with the constructed paths
    compare_and_flag_files(error_log_file, folder_path)

    print("Finished comparing files. Check 'missing_files.txt' and 'matched_files.txt' for results.")
