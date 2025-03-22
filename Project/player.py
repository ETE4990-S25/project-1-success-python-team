import json
import os

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

    def save_profile(self, filename="data/player.json"):
        """Saves player data to JSON, ensuring the folder exists."""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=4)
        print("💾 Player data saved!")

    def load_profile(self, filename="data/player.json"):
        """Loads player data from JSON."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.__dict__.update(data)
            print(f"📂 Loaded player: {self.name}, Level {self.level}, Role: {self.role}")
        except FileNotFoundError:
            print("⚠ No saved player profile found. Starting fresh.")

# 🎭 Player Subclasses

class Warrior(Player):
    """Warrior class - Strong melee fighter with high health."""
    def __init__(self, name):
        super().__init__(name, role="Warrior")
        self.health = 120  # More health
        self.stats["strength"] += 5  # Extra melee power
        self.stats["agility"] += 1  # Lower agility

class Mage(Player):
    """Mage class - Uses magic instead of brute force."""
    def __init__(self, name):
        super().__init__(name, role="Mage")
        self.mana = 100  # More mana
        self.stats["intelligence"] += 6  # High magic power
        self.stats["strength"] -= 2  # Weak physical attacks

class Rogue(Player):
    """Rogue class - Fast, agile fighter with critical hits."""
    def __init__(self, name):
        super().__init__(name, role="Rogue")
        self.stats["agility"] += 7  # Fast movement & dodging
        self.stats["strength"] += 2  # Decent attack power
        self.stats["intelligence"] -= 2  # Lower magic ability

# Example Usage
if __name__ == "__main__":
    player = Mage("Eldrin")
    player.save_profile()


