import os
from xml.etree import ElementTree as ET

def compare_and_flag_missing(error_log_file="/Users/sayeed/desktop/mini project/error_log.txt",
                             folder_path="/Users/sayeed/desktop/mini project/folder_xml",
                             missing_file_log="/Users/sayeed/desktop/mini project/missing_files.txt"):
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

    # Loop through each line in the error log
    for line in error_lines:
      # Extract the referenced XML file name
      xml_filename = line.strip()  # Remove leading/trailing whitespace

      # Check if the file exists in the folder
      if not os.path.isfile(os.path.join(folder_path, xml_filename)):
        # File not found, flag it
        missing_file.write(f"Missing file: {xml_filename}\n")

      else:
        # Optional: If you want to perform additional processing on existing files,
        # do it here. For example, you could try parsing the XML with:
        #   with open(os.path.join(folder_path, xml_filename), 'r') as xml_file:
        #     xml_tree = ET.parse(xml_file)
        #     # Process the XML tree
        pass

if __name__ == "__main__":
  compare_and_flag_missing()
