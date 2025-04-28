from player import Warrior, Mage, Rogue
from combat import Combat
from world import World
from gameRules import GameRules


def choose_player_type():
    #Prompt for player name and class selection.
    name = input("Enter your character name: ").strip()
    print("\nChoose your class:")
    print("1. Warrior - Strong melee fighter with high health")
    print("2. Mage    - Powerful magic user with high intelligence")
    print("3. Rogue   - Agile, fast, and critical hit specialist")

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


def choose_difficulty():
    
    print("\nChoose Difficulty: Easy, Normal, Hard")
    while True:
        difficulty = input("Enter difficulty: ").strip().capitalize()
        if difficulty in ["Easy", "Normal", "Hard"]:
            return difficulty
        print("Invalid input. Try again.")


def handle_explore(exploration_gen):
    
    event = next(exploration_gen)
    print(f"You explore the world: {event}")


def handle_inventory(player):
    
    print("\nYour Inventory:")
    if not player.inventory:
        print("  (Empty)")
    else:
        for item in player.inventory:
            name = item.get('name', 'Unknown')
            typ = item.get('type', 'Unknown')
            print(f"  - {name} ({typ})")


def handle_combat(player):
    
    battle = Combat(player)
    battle.combat_round()


def main_menu():
    
    # Initialize player and game settings
    player = choose_player_type()
    player.load_profile()

    difficulty = choose_difficulty()
    rules = GameRules(difficulty=difficulty, player_role=player.role)

    # Set up world exploration generator
    world = World()
    exploration = world.event_generator(player)

    # Main loop
    while True:
        print("\nMain Menu:")
        print("1. Explore the world")
        print("2. View inventory")
        print("3. Enter combat")
        print("4. Save & Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_explore(exploration)
        elif choice == "2":
            handle_inventory(player)
        elif choice == "3":
            handle_combat(player)
        elif choice == "4":
            player.save_profile()
            print("Progress saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def start_game():
    #Entry point for starting the game
    main_menu()


if __name__ == "__main__":
    start_game()
