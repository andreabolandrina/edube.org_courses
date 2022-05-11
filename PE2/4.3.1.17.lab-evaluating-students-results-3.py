#!/usr/bin/env python3

# 4.3.1.17 LAB: Evaluating students' results
# 
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements:
#   the student's first name,
#   the student's last name,
#   and the number of point the student received during certain classes.
# 
# The elements are separated with white spaces.
# Each student may appear more than once inside Prof. Jekyll's file.
# 
# The file (samplefile.txt) may look as follows:
# John Smith 5
# Anna Boleyn 4.5
# John Smith 2
# Anna Boleyn 11
# Andrew Cox 1.5
# 
# Your task is to write a program which:
#   asks the user for Prof. Jekyll's file name;
#   reads the file contents and counts the sum of the received points for each student;
#   prints a simple (but sorted) report, just like this one:
# Andrew Cox 1.5
# Anna Boleyn 15.5
# John Smith 7.0

# Note:
#   your program must be fully protected against all possible failures:
#     the file's non-existence, 
#     the file's emptiness, or 
#     any input data failures; 
#   encountering any data error should cause immediate program termination, 
#   and the erroneous should be presented to the user;
# 
#   implement and use your own exceptions hierarchy - we've presented it in the editor; 
#   the second exception should be raised when a bad line is detect, 
#   and the third when the source file exists but is empty.
# 
# Tip: Use a dictionary to store the students' data.

import os

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass

students = {}

try:

    # sourcefile = input('enter the sourcefile path:')
    # filename hard-coded for convenience
    sourcefile = 'PE2/4.3.1.17.lab-evaluating-students-results-3.samplefile.txt'
    
    stream = open(sourcefile, 'rt')
    lines = stream.readlines()
    stream.close()
    
    if len(lines) == 0:
        raise FileEmpty
    
    for line in lines:
        words = line.split()

        if len(words) < 3:
            raise BadLine

        student_id = words[0] + ' ' + words[1]
        
        if student_id in students:
            students[student_id] += float(words[2])
        else:
            students[student_id] = float(words[2])

    print(students)
    for student in sorted(students.keys()):
        print(student, '\t' ,students[student])


except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))
except FileEmpty as e:
    print("File is empty")
except BadLine as e:
    print("Bad Line")
