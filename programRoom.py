from simpleRoomClass import Room

kitchen = Room("Kitchen")
dining_hall= Room("Dining Hall")
ballroom = Room("Ballroom")

kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.link_room(dining_hall, "south")
dining_hall.set_description("A large room with a large fire place")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
ballroom.set_description("A vast room with a large oak polished floor")
ballroom.link_room(dining_hall, "east")

current_room = kitchen

while True:
    print ("\n")
    current_room.get_details()
    command = input(">> Choose a direction ")
    current_room = current_room.move(command)