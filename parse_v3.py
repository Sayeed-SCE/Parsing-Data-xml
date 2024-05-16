import os


def compare_and_flag_files(error_log_file, folder_path, missing_file_log, matched_file_log):
  """
  Compares XML references in an error log with a folder, flags missing files,
  and saves them to separate text files for missing and matched files.

  Args:
      error_log_file (str): Path to the error log file containing XML references.
      folder_path (str): Path to the folder containing the XML files.
      missing_file_log (str): Path to the output text file for missing files.
      matched_file_log (str): Path to the output text file for matched files.
  """

  # Get folder filenames as a set (more efficient for large folders)
  folder_files = set(os.listdir(folder_path))

  # Open files for writing
  with open(missing_file_log, 'w') as missing_file, open(matched_file_log, 'w') as matched_file:
    # Loop through each line in the error log
    for line in open(error_log_file, 'r'):
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
  # Make paths configurable (replace with your actual paths)
  error_log_file = "/Users/sayeed/desktop/mini project/error_log.txt"
  folder_path = "/Users/sayeed/desktop/mini project/folder_xml"
  missing_file_log = "/Users/sayeed/desktop/mini project/missing_files.txt"
  matched_file_log = "/Users/sayeed/desktop/mini project/matched_files.txt"

  compare_and_flag_files(error_log_file, folder_path, missing_file_log, matched_file_log)
