import json

class Player:
    """Base class for player data (loads & saves from JSON)."""
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = 100
        self.mana = 50
        self.level = 1
        self.stats = {"strength": 5, "agility": 3, "intelligence": 4}
        self.inventory = []

    def load_profile(self, filename="data/player.json"):
        """Loads player data from JSON."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.__dict__.update(data)
            print(f"📂 Loaded player: {self.name}, Level {self.level}")
        except FileNotFoundError:
            print("⚠ No saved player profile found. Starting fresh.")

    def save_profile(self, filename="data/player.json"):
        """Saves player data to JSON."""
        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=4)
        print("💾 Player data saved!")

# Example Usage
player = Player("Leon", "Warrior")
player.load_profile()
player.save_profile()
