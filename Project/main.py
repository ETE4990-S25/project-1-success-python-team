from player import Warrior, Mage, Rogue
from inventory import Inventory
from combat import Combat
from world import event_generator
from rules import GameRules

def choose_player_type():
    """Allows the user to select a player type at game start."""
    print("\n🎭 Choose Your Player Type:")
    print("1. 🛡 Warrior - Strong melee fighter with high health")
    print("2. 🔥 Mage - Powerful magic user with high intelligence")
    print("3. 🗡 Rogue - Agile, fast, and critical hit specialist")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        name = input("Enter your character name: ").strip()
        
        if choice == "1":
            return Warrior(name)
        elif choice == "2":
            return Mage(name)
        elif choice == "3":
            return Rogue(name)
        else:
            print("⚠ Invalid choice. Please enter 1, 2, or 3.")

def main_menu():
    """Displays the main menu and handles player choices."""
    print("\n🎮 Welcome to the Adventure Game!")
    
    # Load player profile or create a new one
    player = choose_player_type()
    player.load_profile()

    # Load game difficulty settings
    rules = GameRules("Normal")  # Change to "Easy" or "Hard" as needed

    # Create inventory and exploration generator
    inventory = Inventory()
    exploration = event_generator()

    while True:
        print("\n🔹 Main Menu")
        print("1. Explore the world")
        print("2. View inventory")
        print("3. Enter combat")
        print("4. Save & Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f"🌍 {next(exploration)}")  # Show a random world event
        elif choice == "2":
            print("\n📜 Inventory:")
            for item in player.inventory:
                print(f"🔸 {item['name']} - {item['type']}")
        elif choice == "3":
            battle = Combat(player)
            battle.combat_round()
        elif choice == "4":
            player.save_profile()
            print("💾 Progress saved! Exiting game.")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

