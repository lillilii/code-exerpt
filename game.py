import random
from map import *
from time import *

map = Map()
inventory = []
rooms = []
items = []
descriptions = []
specialRooms = []
currentRoom = 704
end = False

for i in range(999):
    rooms.append(False)
    items.append(False)
    specialRooms.append(False)
    descriptions.append(False)

rooms[704] = "You are in a trench. Tall dirt walls border you to the West, North and East. The trench continues to the south."
rooms[705] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[706] = "A dirt wall borders you to the East. The trench continues to the North, West, and South. There is a small pile of rocks to the West and something shiny farther south"
rooms[707] = "Dirt walls border you to the East and West. The trench continues to the North and South. There is a pile of rubble to the south"
rooms[708] = "Dirt walls border you to the East, West, and South. There is a large pile of rubble."
items[708] = "Grenade"
descriptions[708] = "You find a grenade among the rubble. Enter t to take."
rooms[606] = "Dirt walls border you to the North and South. The trench continues to the East and West. There is a small pile of rocks."
items[606] = "Knife"
descriptions[606] = "There is a knife among the rocks. Enter t to take"
rooms[502] = "You've hit a dead end. The only way out is south."
rooms[503] = "Dirt walls border you to the East and West. The trench continues to the North and South. You bump into a large wooden crate in the dark"
items[503] = "M1 Grand"
descriptions[503] = "You find an M1 Grand in the crate. Enter t to take"
rooms[504] = "Dirt walls border you to the North, East, and West. The trench continues to the South."
rooms[505] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[506] = "A dirt wall borders you to the South. The trench continues to the East, West, and North"
rooms[406] = "You trip over something in the dark, part of the trench has collapsed here. There is a partially buried body. Dirt walls border you to the North and South. The trench continues to the East and West"
items[406] = "note"
descriptions[406] = "The person is clutching a piece of paper. Type t to take"
rooms[301] = "Dirt walls border you to the North and East. The trench continues to the South and West"
rooms[302] = False
rooms[303] = "Dirt walls border you to the West and East. The trench continues to the North and South the ground is littered with bits of metal. The path north is blocked by a wire fence."
specialRooms[1] = 303
rooms[304] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[305] = "Dirt walls border you to the West and East. The trench continues to the North and South"
rooms[306] = "The trench continues to the East, West, North and South"
rooms[307] = "Dirt walls border you to the East, West, and South. The trench continues to the North"
rooms[201] = "Dirt walls border you to the North and South. The trench continues to the East and West"
rooms[206] = "Dirt walls border you to the North and South. The trench continues to the East and West"
rooms[101] = "There is a locked door on the west side."
specialRooms[2] = 101
rooms[106] = "A dirt wall borders you to the North. The trench continues to the East, West and South. There is something littering the ground to the West."
rooms[107] = "You are in an aisle. You can go south or lead north"
rooms[108] = "The ground is littered with bits of metal. You can go south or lead north"
items[108] = "Key"
descriptions[108] = "You spot a key among the bits. Type t to take."
rooms[109] = "You are in an aisle. You can go south or lead north"
rooms[110] = "You are in an aisle. The path south is blocked to the south with a flimsy wooden baricade."
specialRooms[3] = 110
rooms[111] = False
rooms[11] = "A dirt wall is south, north, and west. The only direction is east. Wooden boards litter the ground"
items[11] = "Ladder"
descriptions[11] = "You find a ladder laying among the boards. Enter t to take"
rooms[6] = "Dirt walls border you to the West, North, and South. There are are some metal scraps at your feet."
items[6] = "Ammo"
descriptions[6] = "You find some ammunition on the ground. Enter t to take"
rooms[1] = False
specialRooms[4] = 1

def oneLetterAtATime(text):
    for i in text:
        print(i, end="", flush=True)
        sleep(0.0)

def sroom(srooms, croom, rooms, inventory):
    global end
    if(croom in srooms):
        if(croom == 1):
            if("Ladder" in inventory):
                oneLetterAtATime("The ladder should be able to get you up out of the trench. Use the ladder? ")
                i=input("(y/n) ")
                if(i=="y"):
                    end = True
                    srooms[4]=False
                    oneLetterAtATime("As you make it to the surface, you pass out.")
                    oneLetterAtATime("You wake up in a wagon. Three other prisoners are with you. One of them speaks \"Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there.\"")
                else:
                    currentRoom = 101
            else:
                oneLetterAtATime("Looks like you need a ladder. Look around.")
        if(croom == 101):
            if("Key" in inventory):
                oneLetterAtATime("Looks like the key you have would work. Would you like to use it? ")
                i=input("(y/n) ")
                if(i=="y"):
                    inventory.remove("Key")
                    oneLetterAtATime("the key unlocks the door. \nYou can now continue west.")
                    srooms[1]=False
                    rooms[101]="You are in a doorway. the path continues West and East."
                    rooms[1] ="There's a hatch 10 feet above you going into what looks like a bunker."
                else:
                    currentRoom = 201
            else:
                oneLetterAtATime("Looks like you need a key. Try looking around.")
        if(croom == 110):
            if("Grenade" in inventory):
                oneLetterAtATime("The baricade looks weak enough to be blown apart by a grenade. Use it now? ")
                i=input("(y/n) ")
                if(i=="y"):
                    inventory.remove("Grenade")
                    oneLetterAtATime("You pull the pin and throw the grenade at the baricade. It gets torn apart by the explosion and you are showered with dirt. \nYou can now continue South.")
                    srooms[3]=False
                    rooms[110]="Pieces of board litter the pathway. The path continues North and South."
                    rooms[111]="Dirt walls border you to the East and South. The trench continues to the North and West. There a pile of wooden scraps on the ground to the West."
                else:
                    currentRoom = 109
            else:
                oneLetterAtATime("The baricade is too solid to tear apart with your hands. Maybe if you had some sort of explosive you could blow it up?")
        if(croom == 303):
            if("Knife" in inventory):
                oneLetterAtATime("This barbed wire looks like it could be cut apart with a knife. Use it now? ")
                i=input("(y/n)")
                if(i=="y"):
                    inventory.remove("Knife")
                    oneLetterAtATime("You use the knife to cut through the wire. You get through, but in the process destroy the knife. \nYou can now continue north.")
                    srooms[1]=False
                    rooms[303]="Dirt walls border you to the east and west. Barbed wire litters the passage. The trench continues to the North and South"
                    rooms[302]="The path continues North and South."
                else:
                    currentRoom = 304
        #open for more special rooms like ending, boss battle, etc.

def checkForItem(room, items):
    if(items[room]!=False):
        return True



def move(direction, room):
    if(direction=="t"):
        if(checkForItem(room, items)):
            inventory.append(items[room])
            items[room] = False

    elif(direction=="n"):
        if(rooms[room - 1] == False):
            oneLetterAtATime("Sadly, you can't walk through the ground, or walls.")
        else:
            room -= 1
    elif(direction=="s"):
        if(rooms[room + 1] == False):
            oneLetterAtATime("Sadly, you can't walk through the ground, or walls.")
        else:
            room += 1
    elif(direction=="e"):
        if(rooms[room + 100] == False):
            oneLetterAtATime("Sadly, you can't walk through the ground, or walls.")
        else:
            room += 100
    elif(direction=="w"):
        if(rooms[room - 100] == False):
            oneLetterAtATime("Sadly, you can't walk through the ground, or walls.")
        else:
            room -= 100
    return room

def itemInRoom(room, items, desc):
    if(items[room] != False):
        print(desc[room])

oneLetterAtATime("You are an allied soldier fighting in world war 2 on the beaches. You got hit by an explosion and got push into a trench, luckly you survive becuase you landed on a sand bag. Now you have to fight your way out.\n")
while not end:
    map.draw(rooms, False, currentRoom)
    oneLetterAtATime(rooms[currentRoom])
    oneLetterAtATime("\nInventory: "+str(inventory)+"\n")
    checkForItem(currentRoom, items)
    sroom(specialRooms, currentRoom, rooms, inventory)
    itemInRoom(currentRoom, items, descriptions)
    oneLetterAtATime("n to go North, s for South, e for East, w for West.\n")
    i=input("What do you want to do? ")
    print("")
    if(i=="crash"):
        print("A Fatal Error Has Occured")
        break
    currentRoom=move(i, currentRoom)
    if(end is True):
        break
while True:
    i=1
