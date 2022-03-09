#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Data Types Lab

varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]

print(f"{varString[3:30:1]} \n{varString[0:3:1]} \n{varString[3:12:1]} \n{varString[0:30:2]} \n{varString[::-1]}") 
print(f"\n{varList[::-1]} \n{varList[2::-1]} \n{varList[2:4:]} \n{varList[::3]} \n{varList[1::]}")
for x in varString:
    print(f"{x}")
for x in varList:
    print(f"{x}")
