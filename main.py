from engine import GameEngine
from rooms import Room
from characters import Player, Enemy
from items import Evidence

#create rooms
enterance = Room("Enterance", "The enterance of the suspect's house. You can leave from here, but if you don't have three pieces of evidence\n"
                 "you won't be able to catch the suspect.")
landing_room = Room("Landing Room", "A small room where a couple of bedrooms connect. You also see an open arch to the east that leads to the kitchen.")
gathering_room = Room("Gathering Room", "A business-like room with a desk and some chairs. Looks like it used to hold meetings.")
kitchen = Room("Kitchen", "A standard kitchen in appearance, however a foul odor fills the room.")
west_bedroom = Room("Western Bedroom", "A disheveled bedroom. The bed appears to have been slept in recently.")
north_bedroom = Room("North Bedoom", "A small, simple bedroom. Looks like it is used for guests.")
living_room = Room("Living Room", "A room for hosting friends and family.")
dining_room = Room("Dining Room", "A dining room. There is a table set for one.")
master_bedroom = Room("Master Bedroom", "The suspect's bedroom. Something doesn't seem right here.")
bathroom = Room("Bathroom", "A bathroom. There is a rancid smell filling the room.")

#create characters
player = Player("Investigator", "This is the protag", enterance)
enemy= Enemy("Suspect", "This is the antag", master_bedroom)

#create Evidence
wallet = Evidence("Wallet", "A leather wallet. The ID inside matches the latest missing victim.")
watch = Evidence("Watch", "A custom engraved watch with the name of one of the missing people.")
calendar = Evidence("Calendar", "A monthly calender. There is an 'X' on each day that a victim has gone missing.")


#add exits/connection points between rooms
enterance.add_exit("north", landing_room)
enterance.add_exit("east", gathering_room)
landing_room.add_exit("north", north_bedroom)
landing_room.add_exit("east", kitchen)
landing_room.add_exit("south", enterance)
landing_room.add_exit("west", west_bedroom)
west_bedroom.add_exit("east", landing_room)
north_bedroom.add_exit("south", landing_room)
kitchen.add_exit("east", dining_room)
kitchen.add_exit("south", gathering_room)
kitchen.add_exit("west", landing_room)
dining_room.add_exit("north", bathroom)
dining_room.add_exit("south", living_room)
dining_room.add_exit("west", kitchen)
bathroom.add_exit("south", dining_room)
gathering_room.add_exit("north", kitchen)
gathering_room.add_exit("east", living_room)
gathering_room.add_exit("west", enterance)
living_room.add_exit("north", dining_room)
living_room.add_exit("east", master_bedroom)
living_room.add_exit("west", gathering_room)
master_bedroom.add_exit("east", living_room)

#add evidence to rooms
west_bedroom.add_evidence(wallet)
kitchen.add_evidence(watch)
master_bedroom.add_evidence(calendar)


#start the game
if __name__ == "__main__":
    game = GameEngine(start_room = enterance, player=player, enemy=enemy)
    game.play()