1. How to Generate and Open EPUB File
This guide will walk you through the steps to generate and open an EPUB file using the provided Python script. Please follow the instructions carefully.

2. Prerequisites:
2a. Python Installation:
   - If Python is not installed on your system, download and install Python 3 from the official website: [Python Downloads](https://www.python.org/downloads/).
   - During installation, make sure to check the option that adds Python to the system PATH.

   Example Install Path: "C:\Python311" (or "C:\Program Files\Python")

   > Note: If you already have Python installed, you can skip this step.



3. Steps:

3a. Download the Script:  <== TODO:script name does not match
   - Download the script file "create_epub_script.py" to your computer.

3b. Create a Folder for Your Ebook:
   - Create a new folder to organize your ebook-related files. For example, create a folder on your "C:" drive, such as "C:\MyEbook".

3c. Place Your Content:
   - Place the text files containing your content (e.g., chapters) inside the folder created in the previous step.

4. Open Command Prompt:
   - Press "Win + R", type "cmd", and press Enter to open the Command Prompt.

5. Navigate to Your Script:
   - Use the "cd" command to navigate to the folder containing the script.
     """bash
     cd C:\Path\To\Your\Script
     """

6. Run the Script:
   - Run the Python script by typing the following command and pressing Enter.
     """bash  <== TODO : remove these
     python create_epub_script.py
     """
     If you installed Python in a different location, provide the full path to the Python executable.
     """bash
     C:\Python311\python.exe create_epub_script.py
     """

   > Note: The script will generate an EPUB file named "Adyathana2(WasanthaKKGee).epub" in the same folder.

7. Open the EPUB File:
   - Navigate to the folder where the EPUB file is generated (e.g., "C:\MyEbook").
   - Double-click on the "Adyathana2(WasanthaKKGee).epub" file to open it with the default associated EPUB viewer or Calibre's viewer if you have Calibre installed.

Congratulations! You have successfully generated and opened your EPUB file. If you encounter any issues or have questions, feel free to seek assistance on relevant forums or communities.



# EPUB Creation Script

This Python script converts a collection of Sinhala text files into an EPUB format using the EbookLib library.

## Requirements

Ensure that you have the required library installed:

"""bash
pip3 install EbookLib



Usage

    Put your book folders inside the 'input' folder.

    After running the script, the EPUB file is created in the 'output' folder.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Working Examples

1. absolute path
cd C:\tmp\LakshithaWarnamal\EbookCreation
C:\Python311\python scripts\main.py C:\tmp\LakshithaWarnamal\EbookCreation\input\Adyathana2(WasanthaKKGee)-SamudraW
output : ePub is created in C:\tmp\LakshithaWarnamal\EbookCreation\output

2. relative path
cd C:\tmp\LakshithaWarnamal\EbookCreation
C:\Python311\python scripts\main.py input\Adyathana2(WasanthaKKGee)-SamudraW
output : ePub is created in C:\tmp\LakshithaWarnamal\EbookCreation\output

+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Developer notes : 

This Python script converts a collection of Sinhala text files into an EPUB format. It uses the EbookLib library to generate the EPUB file.

import os
import re
import subprocess
import logging
from datetime import datetime
from ebooklib import epub

# ... (rest of the script remains unchanged)

Ensure that you remove unnecessary spaces, blank lines, and the section about cloning or downloading the repository from the README file. The provided README now contains only essential information and examples.