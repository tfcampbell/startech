from Room import Room
from Character import Enemy

print("Play the zombie game")

#create three rooms
kitchen = Room("Kitchen")
dining_hall= Room("Dining Hall")
ballroom = Room("Ballroom")

#set the description and the direction link to other room
kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.link_room(dining_hall, "south")
dining_hall.set_description("A large room with a large fire place")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
ballroom.set_description("A vast room with a large oak polished floor")
ballroom.link_room(dining_hall, "east")

#create an enemy
dave = Enemy("Dave" , "A smelly zombie")
dave.set_conversation("Brrlgrh...rghl...brains...")
dave.set_weakness("Cheese")

#add a character to the room
dining_hall.set_character_in_room(dave)


#current room on start
current_room = kitchen

#play game
while True:
    print ("\n")
    current_room.get_details()
    inhabitant = current_room.get_character_in_room()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">> Choose a direction ")
    current_room = current_room.move(command)