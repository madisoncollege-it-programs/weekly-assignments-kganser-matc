#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Midterm slicing project

print("Name: Kaden Ganser")
hFile = open("slicing-file.txt", "r")
mySlice = hFile.readline()

word1 = mySlice[1::]
word2 = mySlice[2:1:4]
word3 = mySlice[9:2:12]
word4 = mySlice[10:12]
word5 = mySlice[::-3]

print(f"{word2}")
hFile.close()
