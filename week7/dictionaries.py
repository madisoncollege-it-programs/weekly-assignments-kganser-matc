#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Dictionaries Lab

serverDict = {"server1.testlab.com":"192.168.1.10", "server2.testlab.com":"192.168.1.11", "server3.testlab.com":"192.168.1.12", "server4.testlab.com":"192.168.1.13", "server5.testlab.com":"192.168.1.14", "server6.testlab.com":"192.168.1.15"}
print(serverDict.keys())
print(serverDict.values())
print(serverDict.items())
serverDict["server7.testlab.com"] = "192.168.1.16"
serverDict["server8.testlab.com"] = "192.168.1.17"
print("server2.testlab.com" in serverDict)
print("server8.testlab.com" in serverDict)
