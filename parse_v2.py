import os


def compare_and_flag_missing(error_log_file, folder_path, missing_file_log):
  """
  Compares XML references in an error log with a folder, flags missing files,
  and saves them to a text file.

  Args:
      error_log_file (str): Path to the error log file containing XML references.
      folder_path (str): Path to the folder containing the XML files.
      missing_file_log (str, optional): Path to the output text file for missing files. Defaults to "missing_files.txt".
  """

  # Open error log file
  with open(error_log_file, 'r') as f:
    error_lines = f.readlines()

  # Open missing file log for writing
  with open(missing_file_log, 'w') as missing_file:

    # Get folder filenames as a set (more efficient for large folders)
    folder_files = set(os.listdir(folder_path))

    # Loop through each line in the error log
    for line in error_lines:
      # Extract the referenced XML filename (assuming filename only, no path)
      xml_filename = line.strip().split('/')[-1]  # Extract last part (filename)

      # Check if the file exists in the folder using membership in the set
      if xml_filename not in folder_files:
        # File not found, flag it
        missing_file.write(f"Missing file: {xml_filename}\n")

  # Optional: If you want to perform additional processing on existing files,
  # do it here. For example, you could try parsing the XML with:
  #   with open(os.path.join(folder_path, xml_filename), 'r') as xml_file:
  #     xml_tree = ET.parse(xml_file)
  #     # Process the XML tree
  pass


if __name__ == "__main__":
  # Make paths configurable (replace with your actual paths)
  error_log_file = "/Users/sayeed/desktop/mini project/error_log.txt"
  folder_path = "/Users/sayeed/desktop/mini project/folder_xml"
  missing_file_log = "/Users/sayeed/desktop/mini project/missing_files.txt"

  compare_and_flag_missing(error_log_file, folder_path, missing_file_log)
