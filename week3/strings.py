#!/usr/bin/env python3
import sys

#Author: Kaden Ganser
#Description: String formatting lab

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print(f"Hello {varName: <0s}")
print(f"{varRed: <0s}-{varGreen: <0s}-{varBlue: <0s}")
print(f"Is this {varGreen.lower(): <0s} or {varBlue.lower(): <0s}?")
print(f"My name is {varName.upper()}")
print(f"[{varRed:+^7s}]")
print(f"[{varGreen.lower():=<7}]")
print(f"[{varBlue.lower():*>9s}]")
print(f"{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}{varBlue: <0s}")
print(f"{varLoot}")
print(f"{varLoot: <.1f}")
print(f"I have ${varLoot: <.2f}")
print(f"[{varRed:$^10s}][{varGreen:$^10s}][{varBlue:$^10s}]")
print(f"[{varRed[::-1]: ^7s}][{varGreen: ^7s}][{varBlue[::-1]: ^7s}]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
