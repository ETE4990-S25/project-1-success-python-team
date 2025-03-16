import json

class GameRules:
    """Loads game difficulty settings from JSON."""
    def __init__(self, difficulty="Normal"):
        self.difficulty = difficulty
        self.load_rules()

    def load_rules(self, filename="data/game_rules.json"):
        """Loads difficulty settings from JSON."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.__dict__.update(data.get(self.difficulty, {}))
            print(f"🎮 Game Mode: {self.difficulty}")
            print(f"⚔ Enemy Damage Multiplier: {self.enemy_damage_multiplier}")
        except FileNotFoundError:
            print("⚠ No game rules file found. Using default settings.")

# Example Usage
rules = GameRules("Hard")
rules.load_rules()
