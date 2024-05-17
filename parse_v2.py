# Import the os module for interacting with the operating system
import os

# Define a function named compare_and_flag_missing with three arguments
def compare_and_flag_missing(error_log_file, folder_path, missing_file_log):
    """
    Compares XML references in an error log with a folder, flags missing files,
    and saves them to a text file.

    """

    # Open the error log file in read mode
    with open(error_log_file, 'r') as f:
        # Read all lines from the error log file into a list
        error_lines = f.readlines()

    # Open the missing file log in write mode
    with open(missing_file_log, 'w') as missing_file:
        
        # Get all filenames in the folder and convert them to a set for efficient lookup
        folder_files = set(os.listdir(folder_path))

        # Loop through each line in the error log
        for line in error_lines:
            # Extract the referenced XML filename by removing leading/trailing whitespace
            # and taking only the last part of the path (filename)
            xml_filename = line.strip().split('/')[-1]

            # Check if the file exists in the folder by checking membership in the set
            if xml_filename not in folder_files:
                # If the file does not exist, write a message to the missing file log
                missing_file.write(f"Missing file: {xml_filename}\n")
    pass

# Main execution block to run the function if the script is executed directly
if __name__ == "__main__":
    # Define paths for the error log file, folder containing XML files, and the output log
    # Replace these paths with your actual paths
    error_log_file = "/Users/sayeed/desktop/mini project/error_log.txt"
    folder_path = "/Users/sayeed/desktop/mini project/folder_xml"
    missing_file_log = "/Users/sayeed/desktop/mini project/missing_files.txt"

    # Call the compare_and_flag_missing function with the defined paths
    compare_and_flag_missing(error_log_file, folder_path, missing_file_log)
