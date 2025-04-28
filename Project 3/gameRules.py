import json
import os

class GameRules:
    

    def __init__(self, difficulty="Normal", player_role="Warrior", rules_filename="data/game_rules.json"):
        self.difficulty = difficulty
        self.player_role = player_role
        self.rules_filename = rules_filename
        self.enemy_damage_multiplier = 1.0
        self.xp_multiplier = 1.0
        self.item_drop_rate = 1.0
        self.starting_gold = 100
        self.load_rules()

    def load_rules(self):
        
        if not os.path.exists(self.rules_filename):
            self.create_default_rules()

        try:
            with open(self.rules_filename, "r") as f:
                data = json.load(f)

            # Get ruleset for the selected difficulty level
            ruleset = data.get(self.difficulty, {})
            self.enemy_damage_multiplier = ruleset.get("enemy_damage_multiplier", 1.0)
            self.xp_multiplier = ruleset.get("xp_multiplier", 1.0)
            self.item_drop_rate = ruleset.get("item_drop_rate", 1.0)
            self.starting_gold = ruleset.get("starting_gold", 100)

            self.apply_role_modifiers()
            print(f" Game Mode: {self.difficulty}, Role: {self.player_role}")
            print(f" Enemy Damage Multiplier: {self.enemy_damage_multiplier}")

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f" Error loading rules: {e}. Using default settings.")

    def apply_role_modifiers(self):
        #Modifies game rules based on player type (Warrior, Mage, or Rogue)
        if self.player_role == "Warrior":
            self.enemy_damage_multiplier *= 0.9
            self.xp_multiplier *= 0.8
        elif self.player_role == "Mage":
            self.enemy_damage_multiplier *= 1.2
            self.xp_multiplier *= 1.5
        elif self.player_role == "Rogue":
            self.enemy_damage_multiplier *= 1.0
            self.item_drop_rate *= 0.8

    def create_default_rules(self):
        #Creates default game rules if the rules JSON file is missing
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
        os.makedirs(os.path.dirname(self.rules_filename), exist_ok=True)
        with open(self.rules_filename, "w") as f:
            json.dump(default_rules, f, indent=4)
        print(" Default game rules created.")

# Example usage
if __name__ == "__main__":
    rules = GameRules(difficulty="Hard", player_role="Mage", rules_filename="data/game_rules.json")
    rules.load_rules()
