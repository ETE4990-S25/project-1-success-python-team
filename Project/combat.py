import random
from player import Player

class Combat:
    """Handles turn-based combat mechanics."""
    
    def __init__(self, player):
        self.player = player
        self.enemy = self.generate_enemy()

    def generate_enemy(self):
        """Dynamically generates an enemy with randomized stats."""
ENEMIES = [
    {"name": "Goblin", "health": 50, "attack": 10, "defense": 2, "evasion": 5},
    {"name": "Orc", "health": 80, "attack": 15, "defense": 4, "evasion": 3},
    {"name": "Dark Mage", "health": 60, "attack": 12, "defense": 3, "evasion": 7}
]

def generate_enemy(self):
    return random.choice(ENEMIES).copy()

           {"name": "Goblin", "health": 50, "attack": 10, "defense": 2, "evasion": 5},
           {"name": "Orc", "health": 80, "attack": 15, "defense": 4, "evasion": 3},
           {"name": "Dark Mage", "health": 60, "attack": 12, "defense": 3, "evasion": 7}
        
    return random.choice(enemies)

    def calculate_damage(self, attacker_strength, enemy_defense):
        """Uses expressions to calculate attack damage dynamically."""
        base_damage = attacker_strength * random.uniform(1.2, 1.8)  # Adds some randomness
        final_damage = max(base_damage - enemy_defense, 1)  # Ensure at least 1 damage
        return round(final_damage, 1)

def warrior_crit(self, damage):
    if random.randint(1, 100) <= 20:
        print(f"{self.player.name} lands a **CRITICAL STRIKE** for double damage!")
        self.enemy["health"] -= damage  # Extra hit

def mage_fireball(self):
    if self.player.mana >= 20:
        print(f"{self.player.name} casts **Fireball** on {self.enemy['name']}!")
        self.enemy["health"] -= 15
        self.player.mana -= 20

        
        damage = self.calculate_damage(self.player.stats["strength"], self.enemy["defense"])
        self.enemy["health"] -= damage
        print(f"🗡 {self.player.name} attacks! {self.enemy['name']} loses {damage} HP.")

        # Special Abilities
        if self.player.role == "Warrior" and random.randint(1, 100) <= 20:
            print(f"💥 {self.player.name} lands a **CRITICAL STRIKE** for double damage!")
            self.enemy["health"] -= damage  # Apply extra hit

        if self.player.role == "Mage" and self.player.mana >= 20:
            print(f"🔥 {self.player.name} casts **Fireball** on {self.enemy['name']}!")
            self.enemy["health"] -= 15
            self.player.mana -= 20  # Spend mana

    def enemy_attack(self):
        """Enemy's turn to attack."""
        if random.randint(1, 100) <= self.player.stats.get("agility", 0) * 2:  # Higher agility = better dodge chance
            print(f"💨 {self.player.name} dodged the enemy attack!")
            return

        damage = self.calculate_damage(self.enemy["attack"], self.player.stats.get("defense", 0))
        self.player.health -= damage
        print(f"⚔ {self.enemy['name']} attacks! {self.player.name} loses {damage} HP.")

    def combat_round(self):
        """Runs a single round of combat until someone is defeated."""
        print(f"\n⚔ A wild {self.enemy['name']} appears!")
        
        while self.player.health > 0 and self.enemy["health"] > 0:
            self.player_attack()
            if self.enemy["health"] <= 0:
                print(f"🏆 {self.enemy['name']} defeated!")
                break

            self.enemy_attack()
            if self.player.health <= 0:
                print(f"💀 {self.player.name} was defeated! Game Over.")
                break
