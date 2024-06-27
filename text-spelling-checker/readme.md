Text Spelling Checker
Overview

This Python script is designed to identify and correct typos in a given text file. It utilizes the Spellchecker library to detect misspelled words and offers corrections based on the most likely alternatives. The script takes an input text file, identifies incorrect words, provides correction suggestions, and allows the user to choose a replacement or skip the correction. Finally, it saves the corrected text into an output file.


Author
Lyudvig Asoyan
Date

05.07.2024
Usage
Dependencies

    Python 3.x
    Spellchecker library

Installation

    Ensure you have Python installed on your system.
    Install the Spellchecker library by running:

    pip install spellchecker

Execution

Run the script from the command line, providing the input and output file paths as arguments.

Example:

scss

python spell_checker.py --input_file wrong-text.txt --output_file corrected-text.txt

Command Line Arguments

    --input_file, -f: Path to the input text file containing the text with typos.
    --output_file, -o: Path to the output text file where the corrected text will be saved.

Functionality

    Reads the input text file.
    Identifies misspelled words using the Spellchecker library.
    Offers correction suggestions for each misspelled word, displaying alternatives.
    Allows the user to choose a correction option or skip the correction for each word.
    Saves the corrected text into the specified output file.

Sample Output

The script displays information for each misspelled word, including the original word, suggested correction, and alternative options. The user can input their preferred correction or choose to skip the correction.
Notes

    The script currently supports only text files as input.
    The number of alternative correction options displayed for each word is limited to three.