class Inventory:
    """Manages the player's inventory."""
    def __init__(self):
        self.items = []

    def add_item(self, item_name, item_type, **attributes):
        """Add an item to the inventory."""
        item = {"name": item_name, "type": item_type, **attributes}
        self.items.append(item)
        print(f"👜 {item_name} added to inventory!")

    def use_item(self, player, item_name):
        """Use an item from the inventory."""
        for item in self.items:
            if item["name"].lower() == item_name.lower():
                if item["type"] == "potion":
                    player.health += item.get("heal", 0)
                    print(f"🩹 {player.name} used {item_name} and healed!")
                    self.items.remove(item)
                elif item["type"] == "weapon":
                    print(f"⚔ {player.name} is now wielding {item_name}!")
                return
        print(f"❌ {item_name} not found!")

# Example Usage
inventory = Inventory()
inventory.add_item("Steel Sword", "weapon", damage=20)
