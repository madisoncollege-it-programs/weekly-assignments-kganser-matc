#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: File Data Interactions Lab

hFile = open("/etc/passwd", 'r')
fileinfo = hFile.read()
print(len(fileinfo))
print("The len() function counted the number of characters because it was all saved as a string")
print("You would use this read function because it grabs all of the contents of the file and saves them to a string")
hFile.close()

hFile = open("/etc/passwd", 'r')
fileinfolist = hFile.readlines()
print(len(fileinfolist))
print("The len() function counted the amount of objects in the file because it was saved as a list")
print("You would use this read function over others because it can read all lines and save them as a list")
hFile.close()

with open("/etc/passwd", 'r') as hFile:
    for line in hFile:
        fileinfoloop = hFile.readline()
print(len(fileinfoloop))
print("You would use this technique because it lets you read line by line and save each one, which could be very useful for very large files")
