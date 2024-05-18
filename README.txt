 # Mini Project Parsing DATA

## This project used Python as a programming language. 
To run the project, Type  python3 parse_v1.py or python parse_v2.py in the terminal.
    Make sure to enter the path for xml data folder and Error logs file are correct. 
    
## There are two versions of this mini project.
   - Version 1 only enters the missing data into the missig text file in directory.
   - Version 2 generates two files every that we run the code.
        a. Missed files
        b. Matched or existed file

## parse_v1.py is version-1 just populate the text file with missed files.
    This version 1 identifies missing XML files referenced in an error log. 
    It compares the filenames listed in the error log with the actual files present in a specified folder.

    Run the script from your terminal: python3 parse_v1.py
    The script will prompt you for the directory containing the error log and the folder name containing the XML files.
    Once finished, a "missing_files.txt" file will be generated in the same directory as the script.

## parse_v2.py
    This version 2 compares XML references in an error log with a folder, identifying missing files. 

    It generates separate text files named with timestamps (e.g., missing_files_2024-05-17_16-15-00.txt) to list missing and matched files.  
    The script prompts the user for the directory containing the error log and the folder name containing the XML files.

    The script assumes the error log file contains references to XML files by filename only (no path information).
    It efficiently checks for file existence using a set of filenames retrieved from the specified folder.
    The script uses context managers (`with open(...)`) to ensure proper file opening and closing. 

