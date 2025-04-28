import random

class World:
    

    def __init__(self):
        # Initialize list of possible events
        self.events = [
            "You found a treasure chest!",
            "A wild beast appears!",
            "You discovered an ancient ruin."
        ]
    
    def event_generator(self, player, max_events=3):
    
        event_count = 0
        while event_count < max_events:
            event = random.choice(self.events)
            event_count += 1

            # Modify event outcomes based on player's stats
            if "wild beast" in event and player.stats["agility"] > 5:
                event += " You managed to escape easily!"
            elif "wild beast" in event and player.stats["strength"] > 5:
                event += " You fought it off and gained some experience!"
            
            yield event

# Example Usage

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {"strength": 5, "agility": 3, "intelligence": 4}

# Simulating a player and exploration
player = Player("Eldrin")
world = World()

exploration = world.event_generator(player)
for event in exploration:
    print(event)
