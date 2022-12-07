import sys
import re

# Set these as the file path 
with open("input.txt") as input_file, open("output.txt", "w") as output_file:
    # Read the entire contents of the input file
    text = input_file.read()
    
    # Remove all blank lines and line breaks
    text = re.sub(r"\n+", " ", text)
    
    # Split the text into a list of words
    words = text.split()
    
    # Initialize a counter variable to keep track of the number of words processed
    word_count = 0
    
    # Iterate over the words in the list
    for word in words:
        # Write the word to the output file
        output_file.write(word)
        
        # Increment the word count
        word_count += 1
        
        # If we've processed 100 words, add a line break and a * to the output
        if word_count % 100 == 0:
            output_file.write("\n*********\n")
        
        # Add a space after the word, unless it's the last word
        if word_count != len(words):
            output_file.write(" ")
