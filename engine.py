import os

class GameEngine:
    # init all elements
    def __init__(self, start_room, player, enemy):
        self.current_room = start_room
        self.player = player
        self.enemy = enemy
        self.running = True

    # show game text and then run game loop
    def play(self):
        os.system("cls")
        print("Welcome to the game!\n")
        print("You are a detective looking into the disappearance of some people.\nYou have found the suspect's home "
              "but, they are home and you need to collect three pieces of evidence without getting caught.")
        print("\n+RULES: Every time you take an action, the enemy will move rooms.")
        print("+ACTIONS:"
              "\n Move by inputting a direction (north, east, south, or west)"
              "\n look (investigates the room for clues)"
              "\n inventory (lists any clues you may have found)"
              "\n quit (quit the game)"
              "\n leave (leave the house. Only usable at the 'Enterance'.\n")
        while self.running:
            self.show_room_description()
            self.process_player_input() # player may end loop by choosing to quit here
            if self.running:
             self.update_enemy()
             self.check_interactions()
 
    # prints the room description
    def show_room_description(self):
        # Show the current room's description and exits
        print(f"\nYou are in the {self.player.current_room.name}.")
        print(self.player.current_room.description)
        print(f"Exits: {', '.join(self.player.current_room.exits.keys())}")

    
    # Process the input from player. Supported commands are directions, look, inventory, leave, and quit.
    def process_player_input(self):
        command = input("\n> ").strip().lower()
        if command in self.player.current_room.exits:
            self.player.move(command)
        elif command == "look":
            self.player.look()
        elif command == "inventory":
            self.player.show_inventory()
        elif command == "leave":
            if self.player.current_room.name != "Enterance":
                print("You have to be at the Enterance to leave!")
            elif self.player.leave():
                print("Congratulations! You were able to escape with the evidence!")
                print("You Win!")
                self.running = False
            elif not self.player.leave():
                print("You were able to escape without getting caught, but you don't have enough evidence.")
                print("You lose.")
                self.running = False
            else:
                print("ERROR: leave bug found.")
        elif command == "quit":
            print("Thanks for playing!")
            self.running = False
        else:
            print("Invalid command. Try a direction, 'look', or 'quit'")

    # Updates the enemy in response to player action
    def update_enemy(self):
        self.enemy.patrol() # moves enemy to an adjacent room

    # Check different interactions between objects
    def check_interactions(self):
        if self.player.current_room == self.enemy.current_room:
            print(f"\n{self.player.name} was caught by the {self.enemy.name}!"
                    "\n You Lose!")
            self.running = False