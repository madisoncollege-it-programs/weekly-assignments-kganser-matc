#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Celsius to Fahrenheit Lab

def c2f(celsius):
    fahrenheit = (celsius * 9/5) +32
    return fahrenheit

def main():
    celsius = int(input("Enter a temperature in Celsius: "))
    print(f"The temperature in fahrenheit is: {c2f(celsius)}")

if __name__ == "__main__":
    main()
