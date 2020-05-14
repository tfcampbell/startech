class Room():
    #self refers to data within the object Room
    #None gives no default value
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms ={}
        
    def set_description(self, room_description):
            self.description= room_description
            
    def get_description(self):
            return self.description
        
    def set_name(self, room_name):
        self.name = room_name
        
    def get_name(self):
        return self.name

        
    def describe(self):        
        print(self.description)
        
    #add a method to link the rooms together
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        
    #report room name, description and directions to linked rooms
        
    def get_details(self):
        print(self.name)
        print("------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.name + " is " + direction)
            
    #set up a move function
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way ")
            return self
        
            
        
        