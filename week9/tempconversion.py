#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Temp conversion lab

import f2c
import c2f

measurement = input("Is your temperature in Celsius (C) or Fahrenheit (F)?: ")
temp = int(input("Please enter your temperature: "))

if measurement == "F":
    print(f"The temperature in celsius is: {f2c.f2c(temp)}")

elif measurement == "C":
    print(f"The temperature in fahrenheit is: {c2f.c2f(temp)}")
