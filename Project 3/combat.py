import random
from player import Player

# ===== Constants =====
ENEMIES = [
    {"name": "Goblin", "health": 50, "attack": 10, "defense": 2, "evasion": 5},
    {"name": "Orc", "health": 80, "attack": 15, "defense": 4, "evasion": 3},
    {"name": "Dark Mage", "health": 60, "attack": 12, "defense": 3, "evasion": 7}
]

# ===== Combat Class =====
class Combat:
    
    
    def __init__(self, player):
        self.player = player
        self.enemy = random.choice(ENEMIES).copy()

    def calculate_damage(self, attacker_strength, defender_defense):
        
        base_damage = attacker_strength * random.uniform(1.2, 1.8)
        final_damage = max(base_damage - defender_defense, 1)
        return round(final_damage, 1)

    def player_attack(self):
        #Player attacks enemy
        damage = self.calculate_damage(self.player.stats["strength"], self.enemy["defense"])
        self.enemy["health"] -= damage
        print(f"{self.player.name} attacks! {self.enemy['name']} loses {damage} HP.")

        # Role-specific abilities
        self.player.special_attack(self.enemy)

    def enemy_attack(self):
        #Enemy attacks player
        dodge_chance = self.player.stats.get("agility", 0) * 2
        if random.randint(1, 100) <= dodge_chance:
            print(f"{self.player.name} dodged the enemy attack!")
            return

        damage = self.calculate_damage(self.enemy["attack"], self.player.stats.get("defense", 0))
        self.player.health -= damage
        print(f"{self.enemy['name']} attacks! {self.player.name} loses {damage} HP.")

    def combat_round(self):
        
        print(f"A wild {self.enemy['name']} appears!")
        
        while self.player.health > 0 and self.enemy["health"] > 0:
            self.player_attack()
            if self.enemy["health"] <= 0:
                print(f"{self.enemy['name']} defeated!")
                break

            self.enemy_attack()
            if self.player.health <= 0:
                print(f"{self.player.name} was defeated! Game Over.")
                break

# ===== Player Classes =====
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior")
        self.stats["strength"] += 5
        self.stats["defense"] += 2

    def special_attack(self, enemy):
        if random.randint(1, 100) <= 20:  # 20% crit chance
            print(f"{self.name} lands a critical strike!")
            damage = random.randint(10, 20)
            enemy["health"] -= damage
            print(f"Critical strike deals {damage} bonus damage!")

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage")
        self.stats["mana"] = 50  # Assume mana is in stats

    def special_attack(self, enemy):
        if self.stats.get("mana", 0) >= 20:
            print(f"{self.name} casts Fireball!")
            damage = 15
            enemy["health"] -= damage
            self.stats["mana"] -= 20
            print(f"Fireball deals {damage} damage!")

class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, "Rogue")
        self.stats["agility"] += 5

    def special_attack(self, enemy):
        if random.randint(1, 100) <= 25:  # 25% chance to double strike
            print(f"{self.name} lands a double strike!")
            damage = random.randint(5, 10)
            enemy["health"] -= damage
            print(f"Double strike deals {damage} bonus damage!")

# ===== Character Creation =====
def create_character():
    
    name = input("Enter your character name: ").strip()
    
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return Warrior(name)
        elif choice == "2":
            return Mage(name)
        elif choice == "3":
            return Rogue(name)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
