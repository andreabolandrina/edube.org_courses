#!/usr/bin/env python3

# 4.3.1.16 LAB: Sorted character frequency histogram
# The previous code (lab) needs to be improved. It's okay, but it has to be better.
# 
# Your task is to make some amendments, which generate the following results:
#   the output histogram will be sorted based on the characters' frequency 
#     (the bigger counter should be presented first)
#   the histogram should be sent to a file with the same name as the input one, 
#     but with the suffix '.hist' (it should be concatenated to the original name)
# 
# Assuming that the input file (samplefile.txt) contains just one line filled with:
# cBabAa
# 
# the expected output should look as follows:
# a -> 3
# b -> 2
# c -> 1
# 
# Tip: Use a lambda to change the sort order.

import os
import string

# filename hard-coded for convenience
sourcefile = 'PE2/4.3.1.16.lab-sorted-character-frequency-histogram-4.samplefile.txt'
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

    stream = open(sourcefile + '.hist', 'wt')
    for ch_tup in sorted(alphabet.items(), key=lambda item: item[1], reverse=True):
        if ch_tup[1] > 0:
            # print(ch_tup[0] + " -> " + str(ch_tup[1]))
            stream.write(ch_tup[0] + " -> " + str(ch_tup[1]) + "\n")
        else:
            break
    stream.close()

except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))