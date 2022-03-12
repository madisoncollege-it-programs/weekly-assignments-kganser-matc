#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Midterm if project

print("Name: Kaden Ganser")

Total = 0

hFile = open("Midterm-if.txt", "r")
midtermif = hFile.readlines()

if "gmeach18@ed.gov" in midtermif:
    getLineNumber()
    print(getLineNumber())
elif "248.253.63.149" in midtermif:
    Total += getLineNumber()

print(f"{Total}")
