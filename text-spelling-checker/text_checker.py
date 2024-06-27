"""
This code uses  libraries Spellchecker,
and argparse,
the code is written in order to find typos,
in the text and help correct them

Author Lyudvig Asoyan
Date, 05.07.2024

"""

# Import necessary libraries
import argparse
from spellchecker import SpellChecker

# Function to perform spell checking on a text file
def spell_check(input_file,output_file):
    # Initialize SpellChecker
    spell = SpellChecker()

    # Open input file for reading
    with open(input_file,'r') as file:
        # Read lines from the input file
        file_lines = file.readlines()

        # Initialize result variable to store corrected text
        result = ''

        # Iterate through each line in the file
        for line in file_lines:
            # Split line into words
            content = line.split()

            # Iterate through each word in the line
            for word in content:
                # Check if word is not in the spell checker's dictionary
                if word not in spell:
                    # Get the corrected version of the word
                    correction = spell.correction(word)

                    # Get the three most probable variants for the word
                    variants = list(spell.candidates(word))[:3]
                    # Print information about the word and its variants
                    print("===================")
                    print(f"sentence: {result}")
                    print(f"wrong word: {word}")
                    print(f"corrected word: {correction}")
                    print(f"variants words: {', '.join(variants)}")
                    # Ask user to choose a variant or provide their own correction
                    variant = input("Write your variant, or press Enter to skip: ")

                    # If user provides a variant
                    if variant:
                        # If the variant is a number, choose the corresponding variant from the list
                        if variant.isdigit():
                            result += variants[int(variant)-1] + " "
                        else:
                            # Otherwise, use the provided variant
                            result += variant + " "
                    else:
                        # If user skips, use the corrected word
                        result += correction + " "
                else:
                    # If word is already in the dictionary, use it as it is
                    result += word + " "

            # Add newline after processing each line
            result += "\n"

    # Open output file for writing and save the corrected text
    with open(output_file,'w') as output_file:
        output_file.write(result+'\n')

    # Print message indicating the corrected text has been saved
    print("Corrected text saved in", output_file)


# Function to parse command-line arguments
def arg_parser():
    # Initialize argument parser with description
    parser = argparse.ArgumentParser(description="Text spelling checker")
    # Define command-line arguments for input and output files
    parser.add_argument("--input_file","-f",help='wrong-text',required=True)
    parser.add_argument("--output_file","-o",help='corrected-text',required=True)
    # Parse command-line arguments
    args = parser.parse_args()

    # Call spell_check function with input and output file paths
    spell_check(args.input_file,args.output_file)


# Call the argument parser function to start the program
arg_parser()


# python3 text_checker.py -f wrong-text.txt -o corrected-text.txt