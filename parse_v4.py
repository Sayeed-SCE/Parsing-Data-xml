import os
from datetime import datetime


def compare_and_flag_files(error_log_file, folder_path):
  """
  Compares XML references in an error log with a folder, flags missing files,
  and saves them to separate text files named with timestamps.

  Args:
      error_log_file (str): Path to the error log file containing XML references.
      folder_path (str): Path to the folder containing the XML files.
  """

  # Get current timestamp for filenames
  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

  # Construct filenames with timestamp
  missing_file_log = f"missing_files_{timestamp}.txt"
  matched_file_log = f"matched_files_{timestamp}.txt"

  # Get folder filenames as a set (more efficient for large folders)
  folder_files = set(os.listdir(folder_path))

  # Open files for writing
  with open(missing_file_log, 'w') as missing_file, open(matched_file_log, 'w') as matched_file:
    # Open error log file
    with open(error_log_file, 'r') as error_log:
      for line in error_log:
        # Extract the referenced XML filename (assuming filename only, no path)
        xml_filename = line.strip().split('/')[-1]  # Extract last part (filename)

        # Check if the file exists in the folder using membership in the set
        if xml_filename in folder_files:
          # File found, write to matched file
          matched_file.write(f"Matched file: {xml_filename}\n")
        else:
          # File not found, write to missing file
          missing_file.write(f"Missing file: {xml_filename}\n")


if __name__ == "__main__":
  # Folder and Error log file paths in my local machine configurable
  error_log_file = "/Users/sayeed/desktop/mini project/error_log.txt"
  folder_path = "/Users/sayeed/desktop/mini project/folder_xml"

  compare_and_flag_files(error_log_file, folder_path)
