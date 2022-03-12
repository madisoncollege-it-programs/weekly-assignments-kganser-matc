#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Midterm Jurassic Park Project

print("Name: Kaden Ganser")

password_database = {"Username":"dnedry", "Password":"please"}
command_database = {"reboot": "OK. I will reboot all park systems.", "shutdown": "OK. I will shut down all park systems.", "done": "I hate all this hacker stuff"}

white_rabbit_object = 0
counter = 0

while white_rabbit_object == 0:
    print("Username: ", end ="")
    input_user = input()
    print("Password: ", end ="")
    input_password = input()
    if input_user == "dnedry" and input_password == "please":
        white_rabbit_object += 1
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
    else:
        counter += 1
    if counter >= 3:
        print(f"You didn't say the magic word\n" * 25)

print("Please enter a command", command_database.keys(),": ", end ="")
input_command = input()
if input_command == "reboot":
    print(command_database["reboot"])
elif input_command == "shutdown":
    print(command_database["shutdown"])
elif input_command == "done":
    print(command_database["done"])
else:
    print("The Lysine Contingency has been put into effect")

