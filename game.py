import random
from map import *
#import the enemy class

map = Map()
inventory = []
rooms = []
items = []
specialRooms = []
currentRoom = 704

for i in range(999):
    rooms.append(False)
    items.append(False)
    specialRooms.append(False)

rooms[704] = "You are in a trench. Dirt walls border you to the West, North and East. The trench continues to the south."
rooms[705] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[706] = "A dirt wall borders you to the East. The trench continues to the North, West, and South. There is a small pile of rocks to the West"
rooms[707] = "Dirt walls border you to the East and West. The trench continues to the North and South. There is a pile of rubble to the south"
rooms[708] = "Dirt walls border you to the East, West, and South. There is an object lying in the rubble."
items[708] = "grenade"
rooms[606] = "Dirt walls border you to the North and South. The trench continues to the East and West. There is a small pile of rocks."
items[606] = "knife"
rooms[502] = "You've hit a dead end. The only way out is south."
rooms[503] = "Dirt walls border you to the East and West. The trench continues to the North and South. You bump into a large wooden crate in the dark"
rooms[504] = "Dirt walls border you to the North, East, and West. The trench continues to the South."
rooms[505] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[506] = "A dirt wall borders you to the South. The trench continues to the East, West, and North"
rooms[406] = "You trip over something in the dark, part of the trench has collapsed here. Dirt walls border you to the North and South. The trench continues to the East and West"
items[406] = "dead body"
rooms[301] = "Dirt walls border you to the North and East. The trench continues to the South and West"
rooms[302] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[303] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[304] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[305] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[306] = "A dirt wall borders you to the North. The trench continues to the East, West, and South. There are many shiny objects littering the area to the South."
rooms[307] = "Dirt walls border you to the East, West, and South. The trench continues to the North. There is a large pile of metal scrap around your feet"
items[307] = "key"
rooms[201] = "Dirt walls border you to the North and South. The trench continues to the East and West"
rooms[206] = "Dirt walls border you to the North and South. The trench continues to the East and West"
items[206] = "M1 Grand"
rooms[101] = "There is a locked door on the west side."
specialRooms[1] = 101
rooms[106] = "Dirt walls border you to the North and south. The trench continues to the East and West. There a pile of wooden scraps on the ground to the West."
rooms[107] = "You are in a aisle. You can go south or lead north"
rooms[108] = "You are in a aisle. You can go south or lead north"
rooms[109] = "You are in a aisle. You can go south or lead north"
rooms[110] = "You are in a aisle. You can go south or lead north"
rooms[111] = "Dirt walls border you to the East and South. The trench continues to the North and West. There a pile of wooden scraps on the ground to the West."
rooms[11] = "A dirt wall is south, north, and west. The only direction is east"
rooms[11] = "ladder"
rooms[6] = "Dirt walls border you to the West, North, and South. There are are some wooden scraps at your feet."
items[6] = "ladder"
rooms[1] = False
specialRooms[2] = 1

def sroom(srooms, croom, rooms, inventory):
    if(croom in srooms):
        if(croom == 101):
            if("key" in inventory):
                print("Looks like the key you have would work.")
                i=input("Would you like to use it? (y/n) ")
                if(i=="y"):
                    srooms[1]=False
                    rooms[1] = "there's a hatch 10 feet above you going into what looks like a bunker."
                else:
                    currentRoom = 201
            else:
                print(" Looks like you need a key. Try looking around.")
        #open for more special rooms like ending, boss battle, etc.

def checkForItem(room, items):
    if(room in items):
        print("")

def move(direction, room):
    if(direction=="n"):
        if(rooms[room - 1] == False):
            print("Sadly, you cant walk through the ground, or walls.")
        else:
            room -= 1
    elif(direction=="s"):
        if(rooms[room + 1] == False):
            print("Sadly, you cant walk through the ground, or walls.")
        else:
            room += 1
    elif(direction=="e"):
        if(rooms[room + 100] == False):
            print("Sadly, you cant walk through the ground, or walls.")
        else:
            room += 100
    elif(direction=="w"):
        if(rooms[room - 100] == False):
            print("Sadly, you cant walk through the ground, or walls.")
        else:
            room -= 100
    return room

print("You are an allied soldier fighting in world war 2 on the beaches. You got hit by an explosion and got push into a trench, luckly you survive becuase you landed on sand beg and now you have to fight your way out.  ")
while True:
    map.draw(rooms, False, currentRoom)
    print(rooms[currentRoom])
    checkForItem(currentRoom, items)
    sroom(specialRooms, currentRoom, rooms, inventory)
    i=input("What do you want to do?")
    currentRoom=move(i, currentRoom)
