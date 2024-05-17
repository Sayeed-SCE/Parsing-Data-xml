# Import the os module for interacting with the operating system
import os

def compare_and_flag_missing(error_log_file="/Users/sayeed/desktop/mini project/error_log.txt",
                             folder_path="/Users/sayeed/desktop/mini project/folder_xml",
                             missing_file_log="/Users/sayeed/desktop/mini project/missing_files.txt"):
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
        
        # Loop through each line in the error log
        for line in error_lines:
            # Extract the referenced XML file name by removing leading/trailing whitespace
            xml_filename = line.strip()

            # Check if the file exists in the specified folder
            if not os.path.isfile(os.path.join(folder_path, xml_filename)):
                # If the file does not exist, write a message to the missing file log
                missing_file.write(f"Missing file: {xml_filename}\n")
            else:
                # Optional: Additional processing can be performed if desired. 
                pass

# Main execution block to run the function if the script is executed directly
if __name__ == "__main__":
    compare_and_flag_missing()
