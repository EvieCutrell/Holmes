import random

class Character:
    #generic character data
    def __init__(self, name, description, start_room):
        self.name = name
        self.description = description
        self.current_room = start_room
    

class Player(Character):
    #player also have an inventory
    def __init__(self, name, description, start_room):
        super().__init__(name, description, start_room)
        self.inventory = []

    #investigate the current room for evidence. Update the room if found.
    def look(self):
        print(f"You investiage {self.current_room.name} for evidence.")
        if self.current_room.evidence != None:
            print("You found a piece of evidence!")
            print(f"Description: {self.current_room.evidence.description}")
            self.take_evidence(self.current_room.evidence)
            self.current_room.remove_evidence()
        else:
            print("You didn't find anything of note.")

    #moves the player to a connected room   
    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"{self.name} moves {direction} to the {self.current_room.name}.")

    #adds evidence to inventory
    def take_evidence(self, evidence):
        self.inventory.append(evidence)
        print(f"{evidence.name} evidence has been added to your inventory!")

    #prints the contents of the player's inventory
    def show_inventory(self):
        if self.inventory:
            print("Your inventory contains:")
            for evidence in self.inventory:
                print(f"- {evidence.name}: {evidence.description}")
        else:
            print("Your inventory is empty!")

    #checks win condition if leaving through the enterance
    def leave(self):
        if len(self.inventory) >= 3:
            return True
        else:
            return False


class Enemy(Character):
    def __init__(self, name, description, start_room):
        super().__init__(name, description, start_room)

    #enemy movement
    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"{self.name} moves {direction} to the {self.current_room.name}.")

    #randomize enemy movement to a connected room
    def patrol(self):
        if self.current_room.exits:
            direction = random.choice(list(self.current_room.exits.keys()))
            self.move(direction)
