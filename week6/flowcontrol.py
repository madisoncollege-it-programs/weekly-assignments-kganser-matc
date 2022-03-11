#!/usr/bin/env python3

#Author: Kaden Ganser
#Description: Flow Control Lab

print("""You wake in a dark room with three doors.
Do you go through door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("You walk into a room quickly filling with water")
    print("Think fast, what do you do?\n")

    print("1) Frantically punch the water")
    print("2) Plug the hole in the wall the water seems to be coming from")
    print("3) Drink all of the water")

    # == Water logic ============================
    water = input("-> ")

    if water == "1":
        print("With the spirit of Caligula you punch the water with all your might")
        print("The water retreats, how it happened is not known, but Good Job!")

    if water == "2":
        print("You plug the hole")
        print("That was only one of many holes")

    if water == "3":
        print("You drink all of the water as fast as you can")
        print("You drowned, what did you expect to happen?")

# == Door Number 2 Logic =====================
if  door == "2":
    print("You enter a room filled with multiple versions of yourself")
    
    print("1) Tell yourself off")
    print("2) Ask if you know how to get out")

# == Self Logic ======================
    self = input("-> ")

    if self == "1":
        print("You tell yourself off and leave the room")
        print("Wait which one of you was that?")
    else:
        print("You ask yourself if you know how to leave")
        print("All of you reply yes, and lead you to the exit. That was weird but it worked, Good job!")

# == Door Number 3 Logic ====================
if door == "3":

    print("You walk into a room filled with mold")
    print("What do you want to do?")

    print("1) Set room on fire")
    print("2) Put on a respirator")
    print("3) Eat the mold")

# == Mold Logic =============
    mold = input("-> ")

    if mold == "1":
        print("You lit the room on fire but were unable to make it out in time.")
        print("You could'nt take the heat")

    if mold == "2":
        print("You put on a respirator, but it immediately fails.")
        print("The mold got in, and it won")

    if mold == "3":
        print("You ate all of the mold, every last inch")
        print("The mold grants you amazing powers, mortal life is but a dream now")        
        print(f"\nGood Job!")
