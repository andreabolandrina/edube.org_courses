#!/usr/bin/env python3

# 4.3.1.15 LAB: Character frequency histogram
# A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text.
# Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.
# 
# Your task is to write a program which:
#   asks the user for the input file's name;
#   reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
#   prints a simple histogram in alphabetical order (only non-zero counts should be presented)
# 
# Create a test file for the code, and check if your histogram contains valid results.
# 
# Assuming that the test file (samplefile.txt) contains just one line filled with:
# aBc
# 
# the expected output should look as follows:
# a -> 1
# b -> 1
# c -> 1
# 
# Tip: We think that a dictionary is a perfect data collection medium for storing the counts.
#      The letters may be keys while the counters can be values.

import os
import string

# filename hard-coded for convenience
sourcefile = 'PE2/4.3.1.15.lab-character-frequency-histogram-3.samplefile.txt'
# sourcefile = input('enter the source filename:')

alphabet = {ch:0 for ch in string.ascii_lowercase}

try:
    stream = open(sourcefile, 'rt')
    # works for small files
    content = stream.read()
    stream.close()
    
    for ch in content:
        if ch.isalpha():
            ch = ch.lower()
            alphabet[ch] += 1
    
    for ch in alphabet.keys():
        if alphabet[ch] > 0:
          print(ch + " -> " + str(alphabet[ch]))
    
except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))