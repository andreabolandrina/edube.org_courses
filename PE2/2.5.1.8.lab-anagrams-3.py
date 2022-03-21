#!/usr/bin/env python3

# 2.5.1.8 LAB: Anagrams
# 
# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.
# For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
# 
# Your task is to write a program which:
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# 
# Note:
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent
# 
# Test your code using the data we've provided.
# Test data
# 
# Sample input:
# Listen
# Silent
# 
# Sample output:
# Anagrams
# 
# Sample input:
# modern
# norman
# 
# Sample output:
# Not anagrams


def is_anagram(word1, word2):
    if word1 == '' and word2 == '':
        return False
    
    word1 = sorted(word1.lower().replace(' ', ''))
    word2 = sorted(word2.lower().replace(' ', ''))
    
    i = 0
    while i < len(word1):
        if word1[i] == word2[i]:
            i += 1
            continue
        else:
            return False
    
    return True


word1 = input('Enter your first word, please: ')
word2 = input('Enter your second word, please: ')
if is_anagram(word1, word2):
    print('Anagrams')
else:
    print('Not anagrams')