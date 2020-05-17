from Room import Room
from Character import Enemy
from Character import Character



print("Play the zombie game")
print()

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

#create a player
adv = Character("Player 1", "An intrepid explorer")
adv.set_conversation("Hello, I am an intrepid explorer, who are you? ")


#add a character to the room
dining_hall.set_character_in_room(dave)


#current room on start
current_room = kitchen
adv.describe()

#play game
while True:
    print ("\n")
    #print a description of the current room
    current_room.get_details()
    #if there is a zombie in the room get character detail
    inhabitant = current_room.get_character_in_room()
    if inhabitant is not None:
        inhabitant.describe()
        #interact with character
        adv.talk()
        dave.talk()
        weapon =input("What will you fight with? : ")
        dave.fight(weapon)




    command = input(">> Choose a direction ")
    current_room = current_room.move(command)