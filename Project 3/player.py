import json
import os

class Player:
    
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = 100
        self.mana = 50
        self.level = 1
        self.stats = {"strength": 5, "agility": 3, "intelligence": 4}
        self.inventory = []

        self.load_template(role)

    def load_template(self, role):
    
        try:
            with open("data/player_templates.json", "r") as f:
                templates = json.load(f)
                template = templates.get(role)
                if template:
                    self.health = template["health"]
                    self.mana = template["mana"]
                    self.level = template["level"]
                    self.stats = template["stats"]
        except FileNotFoundError:
            print(" Template file not found! Using default stats.")

    def save_profile(self, filename="data/player.json"):
    
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        data = {
            "name": self.name,
            "role": self.role,
            "health": self.health,
            "mana": self.mana,
            "level": self.level,
            "stats": self.stats,
            "inventory": self.inventory
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Player data saved!")

    def load_profile(self, filename="data/player.json"):
        #Loads player data from JSON
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.name = data["name"]
                self.role = data["role"]
                self.health = data["health"]
                self.mana = data["mana"]
                self.level = data["level"]
                self.stats = data["stats"]
                self.inventory = data["inventory"]
            print(f"Loaded player: {self.name}, Level {self.level}, Role: {self.role}")
        except FileNotFoundError:
            print(" No saved player profile found. Starting fresh.")


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, role="Warrior")

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, role="Mage")

class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, role="Rogue")


if __name__ == "__main__":
    player = Mage("Eldrin")
    player.save_profile()
