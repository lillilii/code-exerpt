import random
#from map import *
from time import *

#map = Map()
inventory = []
rooms = []
items = []
specialRooms = []
currentRoom = 704

for i in range(999):
    rooms.append(False)
    items.append(False)
    specialRooms.append(False)

rooms[704] = "You are in a trench. Tall dirt walls border you to the West, North and East. The trench continues to the south."
rooms[705] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[706] = "A dirt wall borders you to the East. The trench continues to the North, West, and South. There is a small pile of rocks to the West and something shiny farther south"
rooms[707] = "Dirt walls border you to the East and West. The trench continues to the North and South. There is a pile of rubble to the south"
rooms[708] = "Dirt walls border you to the East, West, and South. There is a large pile of rubble."
items[708] = "grenade"
rooms[606] = "Dirt walls border you to the North and South. The trench continues to the East and West. There is a small pile of rocks."
items[606] = "knife"
rooms[502] = "You've hit a dead end. The only way out is south."
rooms[503] = "Dirt walls border you to the East and West. The trench continues to the North and South. You bump into a large wooden crate in the dark"
items[503] = "M1 Grand"
rooms[504] = "Dirt walls border you to the North, East, and West. The trench continues to the South."
rooms[505] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[506] = "A dirt wall borders you to the South. The trench continues to the East, West, and North"
rooms[406] = "You trip over something in the dark, part of the trench has collapsed here. There is a partially buried body. Dirt walls border you to the North and South. The trench continues to the East and West"
items[406] = "note"
rooms[301] = "Dirt walls border you to the North and East. The trench continues to the South and West"
rooms[302] = False
rooms[303] = "Dirt walls border you to the West and East. The trench continues to the North and South the ground is littered with bits of metal. The path north is blocked by a wire fence."
specialRooms[1] = 303
rooms[304] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[305] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[306] = "A dirt wall borders you to the North. The trench continues to the East, West, and South. There are many shiny objects littering the area to the South."
rooms[307] = "Dirt walls border you to the East, West, and South. The trench continues to the North. There is a large pile of metal scrap around your feet"
rooms[201] = "Dirt walls border you to the North and South. The trench continues to the East and West"
rooms[206] = "Dirt walls border you to the North and South. The trench continues to the East and West"
rooms[101] = "There is a locked door on the west side."
specialRooms[2] = 101
rooms[106] = "Dirt walls border you to the North and south. The trench continues to the East and West. There a pile of wooden scraps on the ground to the West."
rooms[107] = "You are in an aisle. You can go south or lead north"
rooms[108] = "You are in an aisle. You can go south or lead north"
items[108] = "key"
rooms[109] = "You are in an aisle. You can go south or lead north"
rooms[110] = "You are in an aisle. The path south is blocked to the south with a flimsy wooden baricade."
specialRooms[3] = 110
rooms[111] = False
rooms[11] = "A dirt wall is south, north, and west. The only direction is east. Wooden boards litter the ground"
rooms[11] = "ladder"
rooms[6] = "Dirt walls border you to the West, North, and South. There are are some metal scraps at your feet."
items[6] = "ammo"
rooms[1] = False
specialRooms[4] = 1

def oneLetterAtATime(text):
    for i in text:
        print(i, end="", flush=True)
        sleep(0.05)

def sroom(srooms, croom, rooms, inventory):
    if(croom in srooms):
        if(croom == 1):
            if("ladder" in inventory):
                oneLetterAtATime("the ladder should be able to get you up out of the trench")
                i=input("Use the ladder? (y/n) ")
                if(i=="y"):
                    srooms[4]=False
                    oneLetterAtATime("as you make it to the surface, you pass out.")
                    oneLetterAtATime("You wake up in a wagon. Three other prisoners are with you. One of them speaks \"Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there.\"")
                else:
                    currentRoom = 101
            else:
                oneLetterAtATime("Looks like you need a ladder. Look around.")
        if(croom == 101):
            if("key" in inventory):
                oneLetterAtATime("Looks like the key you have would work.")
                i=input("Would you like to use it? (y/n) ")
                if(i=="y"):
                    srooms[1]=False
                    rooms[1] = "there's a hatch 10 feet above you going into what looks like a bunker."
                else:
                    currentRoom = 201
            else:
                oneLetterAtATime(" Looks like you need a key. Try looking around.")
        if(croom == 110):
            if("grenade" in inventory):
                oneLetterAtATime("The baricade looks weak enough to be blown apart by a grenade.")
                i=input("use it now? (y/n) ")
                if(i=="y"):
                    srooms[3]=False
                    rooms[111]="Dirt walls border you to the East and South. The trench continues to the North and West. There a pile of wooden scraps on the ground to the West."
                else:
                    currentRoom = 109
            else:
                oneLetterAtATime("The baricade is too solid to tear apart with your hands. Maybe if you had some sort of explosive you could blow it up?")
        if(croom == 303):
            if("knife" in inventory):
                oneLetterAtATime("This barbed wire looks like it could be cut apart with a knife.")
                i=input("use it now (y/n)")
                if(1=="y"):
                    srooms[1]=False
                    rooms[302]="Dirt walls border you to the east and west. Barbed wire litters the passage. The trench continues to the North and South"
                else:
                    currentRoom = 304
        #open for more special rooms like ending, boss battle, etc.

def checkForItem(room, items):
    if(items[room]!=False):
        return True

def move(direction, room):
    if(direction=="t"):
        if(checkForItem(room, items)):
            inventory.add()

    elif(direction=="n"):
        if(rooms[room - 1] == False):
            oneLetterAtATime("Sadly, you cant walk through the ground, or walls.")
        else:
            room -= 1
    elif(direction=="s"):
        if(rooms[room + 1] == False):
            oneLetterAtATime("Sadly, you cant walk through the ground, or walls.")
        else:
            room += 1
    elif(direction=="e"):
        if(rooms[room + 100] == False):
            oneLetterAtATime("Sadly, you cant walk through the ground, or walls.")
        else:
            room += 100
    elif(direction=="w"):
        if(rooms[room - 100] == False):
            oneLetterAtATime("Sadly, you cant walk through the ground, or walls.")
        else:
            room -= 100
    return room

#oneLetterAtATime("You are an allied soldier fighting in world war 2 on the beaches. You got hit by an explosion and got push into a trench, luckly you survive becuase you landed on sand beg and now you have to fight your way out.  ")
while True:
    #map.draw(rooms, False, currentRoom)
    oneLetterAtATime(rooms[currentRoom])
    checkForItem(currentRoom, items)
    sroom(specialRooms, currentRoom, rooms, inventory)
    i=input("\nWhat do you want to do?")
    currentRoom=move(i, currentRoom)
