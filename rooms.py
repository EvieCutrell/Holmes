class Room:
    #init a room
    def __init__(self, name, description, exits = None, evidence = None):
        self.name = name
        self.description = description
        self.exits = exits if exits is not None else {} #dictionary! key: direction, value: destination room
        self.evidence = evidence

    #adds the direction as a key and room as the value
    def add_exit(self, direction, room):
        self.exits[direction] = room

    #returns a list of all the exits
    def get_exits(self):
        return ', '.join(self.exits.keys()) # Returns a list of directions
    
    #adds evidence to a room
    def add_evidence(self, evidence):
        self.evidence = evidence

    #removes evidence from a room when collected
    def remove_evidence(self):
        self.evidence = None

