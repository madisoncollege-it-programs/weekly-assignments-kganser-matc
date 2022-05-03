#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Fahrenheit to Celsius lab

def f2c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    print(f"The temperature in celsius is: {f2c(fahrenheit)}")

if __name__ == "__main__":
    main()
