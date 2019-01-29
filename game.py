import random
#import the enemy class

rooms = []
items = []
currentRoom = 704

for i in range(999):
    rooms.append(False)
    items.append(False)

rooms[704] = "You are in a trench. Dirt walls border you to the West, North and East. The trench continues to the south."
rooms[705] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[706] = "A dirt wall borders you to the East. The trench continues to the North, East, and South. There is something poking out of the dirt to the East"
rooms[707] = "Dirt walls border you to the East and West. The trench continues to the North and South. There is something under a pile of rubble"
rooms[708] = "Dirt walls border you to the East, West, and South. There is an object lying in the rubble."
items[708] = "grenade"
rooms[606] = "Dirt walls border you to the North and South. The trench continues to the East and West. There is something poking out of the dirt by your feet, would you like to pick it up?"
items[606] = "knife"
rooms[504] = "Dirt walls border you to the North, East, and West. The trench continues to the South."
rooms[505] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[506] = "A dirt wall borders you to the South. The trench continues to the East, West, and North"
rooms[406] = "You trip over something in the dark, part of the trench has collapsed here. Dirt walls border you to the North and South. The trench continues to the Easty and West"
items[406] = "dead body"
rooms[306] = "A dirt wall borders you to the North. The trench continues to the East, West, and South. There are many shiny objects littering the area to the South."
rooms[307] = "Dirt walls border you to the East, West, and South. The trench continues to the North. There is a large pile of ammunition around your feet"
items[307] = "ammo"
rooms[206] = "Dirt walls border you to the North and South. The trench continues to the East and West. You bump into a large wooden crate in the dark"
items[206] = "M1 Grand"
rooms[106] = "Dirt walls border you to the North and south. The trench continues to the East and West. There a pile of wooden scraps on the ground to the West."
rooms[6] = "Dirt walls border you to the West, North, and South. There are are some wooden scraps at your feet."
items[6] = "ladder"

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
