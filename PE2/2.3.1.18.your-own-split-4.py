#!/usr/bin/env python3

# 2.3.1.18 Your own split
# 
# Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:
# 
# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()
# 
# Expected output
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []

def mysplit(strng):
    output = []
    tmp = ''
    
    if strng == '':
        return []
    
    for ch in strng:
        if ch != ' ':
            tmp += ch
        elif tmp != '':
            output.append(tmp)
            tmp = ''
    
    if len(tmp) > 0:
        output.append(tmp)
    return output


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))