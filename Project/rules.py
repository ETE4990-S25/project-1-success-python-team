import json
import os

class GameRules:
    """Loads game difficulty settings from JSON."""
    def __init__(self, difficulty="Normal", player_role="Warrior"):
        self.difficulty = difficulty
        self.player_role = player_role
        self.filename = "data/game_rules.json"
        self.load_rules()

    def load_rules(self):
        """Loads difficulty settings from JSON or creates default settings if missing."""
        if not os.path.exists(self.filename):
            self.create_default_rules()  # ✅ Auto-generate game_rules.json if missing

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.__dict__.update(data.get(self.difficulty, {}))
                self.apply_role_modifiers()
            print(f"🎮 Game Mode: {self.difficulty}, Role: {self.player_role}")
            print(f"⚔ Enemy Damage Multiplier: {self.enemy_damage_multiplier}")
        except FileNotFoundError:
            print("⚠ No game rules file found. Using default settings.")

    def apply_role_modifiers(self):
        """Modifies game rules based on player type."""
        if self.player_role == "Warrior":
            self.enemy_damage_multiplier *= 0.9  # Warriors take less damage
            self.xp_multiplier *= 0.8  # Level up slower
        elif self.player_role == "Mage":
            self.enemy_damage_multiplier *= 1.2  # Mages take more damage
            self.xp_multiplier *= 1.5  # Level up faster
        elif self.player_role == "Rogue":
            self.enemy_damage_multiplier *= 1.0  # Normal damage
            self.item_drop_rate *= 0.8  # Rogues find fewer items

    def create_default_rules(self):
        """Creates default game rules if the file is missing."""
        default_rules = {
            "Easy": {
                "enemy_damage_multiplier": 0.8,
                "xp_multiplier": 1.2,
                "item_drop_rate": 1.5,
                "starting_gold": 200
            },
            "Normal": {
                "enemy_damage_multiplier": 1.0,
                "xp_multiplier": 1.0,
                "item_drop_rate": 1.0,
                "starting_gold": 100
            },
            "Hard": {
                "enemy_damage_multiplier": 1.5,
                "xp_multiplier": 0.8,
                "item_drop_rate": 0.7,
                "starting_gold": 50
            }
        }
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "w") as f:
            json.dump(default_rules, f, indent=4)
        print("📜 Default game rules created.")

# Example Usage
rules = GameRules("Hard", "Mage")  # Testing with a Mage
rules.load_rules()




