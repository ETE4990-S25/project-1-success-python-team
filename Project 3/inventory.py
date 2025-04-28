# inventory.py

class Inventory:
    
    
    def __init__(self, items=None):
        self.items = items if items else []

    def add_item(self, item_name, item_type, **attributes):
    
        item = {"name": item_name, "type": item_type, **attributes}
        self.items.append(item)
        print(f"{item_name} added to inventory!")

    def use_item(self, player, item_name):
        
        for item in self.items:
            if item["name"].lower() == item_name.lower():
                if item["type"] == "potion":
                    heal_amount = item.get("heal", 0)
                    player.health += heal_amount
                    player.health = min(player.health, 100)  # Cap health at 100
                    print(f"{player.name} used {item_name} and healed for {heal_amount} HP!")
                    self.items.remove(item)
                elif item["type"] == "weapon":
                    bonus_damage = item.get("damage", 0)
                    player.stats["strength"] += bonus_damage
                    print(f"{player.name} equips {item_name}! Strength increased by {bonus_damage}.")
                    self.items.remove(item)
                return
        print(f"{item_name} not found in inventory.")

    def list_items(self):
        
        if not self.items:
            print("Your inventory is empty.")
        else:
            print("Your Inventory:")
            for item in self.items:
                print(f"- {item['name']} ({item['type']})")


if __name__ == "__main__":
    from player import Mage

    player = Mage("Eldrin")
    inventory = Inventory()

    inventory.add_item("Steel Sword", "weapon", damage=5)
    inventory.add_item("Healing Potion", "potion", heal=30)

    inventory.list_items()
    inventory.use_item(player, "Healing Potion")
    inventory.list_items()
