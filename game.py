import random
#import the enemy class

rooms = []
items = []
currentRoom = 704

for i in range(999):
    rooms.append(False)
    items.append(False)

rooms[704] = "You are in a trench. Dirt walls bordar you to the West, North and East. The treanch continues to the south."
rooms[705] = "Dirt walls border you to the East and West. The trench continues to the North and South"
rooms[706] = ""
rooms[707] = ""
rooms[708] = ""
items[708] = "grenade"
rooms[606] = ""
items[606] = "knife"
rooms[504] = ""
rooms[505] = ""
rooms[506] = ""
rooms[406] = ""
items[406] = "dead body"
rooms[306] = ""
rooms[307] = ""
rooms[206] = ""
rooms[106] = ""
rooms[6] = ""
items[6] = ""

def roomExists()

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
currentRoom = move("n",currentRoom)
