import os  # Imports the `os` module for file system operations

def compare_and_flag_missing(error_log_file, folder_path, missing_file_log):
    """
    Compares XML references in an error log with a folder, flags missing files,
    and saves them to a text file.

    """

    # Open the error log file in read mode with context manager (automatic closing)
    with open(error_log_file, 'r') as f:
        # Read all lines from the error log file into a list
        error_lines = f.readlines()

    # Open the missing file log in write mode with context manager (automatic closing)
    with open(missing_file_log, 'w') as missing_file:

        # Loop through each line in the error log
        for line in error_lines:
            # Extract the referenced XML filename by removing leading/trailing whitespace
            xml_filename = line.strip()

            # Check if the file exists in the specified folder using os.path.isfile
            if not os.path.isfile(os.path.join(folder_path, xml_filename)):
                # If the file does not exist, write a message to the missing file log
                missing_file.write(f"Missing file: {xml_filename}\n")
            else:
                # Optional: Additional processing can be performed if desired.
                pass

# Main execution block to run the function if the script is executed directly
if __name__ == "__main__":
    # Get user input for directory containing error log and folder name
    error_log_dir = input("Enter the directory containing the error log file: ")
    folder_name = input("Enter the name of the folder containing the XML files: ")
    missing_file_log = "missing_files.txt"  # Assuming a fixed name for missing file log

    # Construct full paths based on user input and current working directory
    error_log_file = os.path.join(error_log_dir, "error_log.txt")  # Assuming "error_log.txt" as filename
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Call the function with the constructed paths
    compare_and_flag_missing(error_log_file, folder_path, missing_file_log)

    print("Finished comparing files. Check 'missing_files.txt' for results.")
