def start_game():
    # Initialize the game state variables
    inventory = []
    health = 100
    current_location = "cave"
    print("Welcome to the Lord of Doom!")
    print("Your mission is to explore the mysterious land, find the treasure, and escape with your life!")
    
    while True:
        # Check the player's health to end the game if necessary
        if health <= 0:
            print("You've run out of health and died! The treasure is forever lost")
            break
        
        # Current Location: Cave Entrance
        if current_location == "cave":
            print("\nYou are at the entrance of a dark cave. There are faint screams from within.")
            print("Options:")
            print("(1) Explore deeper into the cave")
            print("(2) Exit to the forest")
            print("(3) Check inventory")
            
            action = input("Choose an option: ")
            if action == "1":
                current_location = "deep_cave"
            elif action == "2":
                current_location = "forest"
            elif action == "3":
                check_inventory(inventory)
            else:
                print("Invalid choice. Try again.")

        # Current Location: Deep Cave
        elif current_location == "deep_cave":
            print("\nYou go deeper into the cave. The air is thick with smoke, and visibility is low.")
            print("You notice something shiny on the ground and a shadow moving in the corner.")
            print("Options:")
            print("(1) Pick up the shiny object")
            print("(2) Approach the shadow")
            print("(3) Go back to the cave entrance")
            
            action = input("Choose an option: ")
            if action == "1":
                if "mysterious gem" not in inventory:
                    inventory.append("mysterious gem")
                    print("You picked up a mysterious gem. It glows faintly in your hand.")
                else:
                    print("You already picked up the gem.")
            elif action == "2":
                print("The shadow turns out to be a dark goblin! It attacks you.")
                health -= 20
                print(f"You managed to escape but lost 20 health. Current health: {health}")
            elif action == "3":
                current_location = "cave"
            else:
                print("Invalid choice. Try again.")

        # Current Location: Forest
        elif current_location == "forest":
            print("\nYou are now in a quiet forest. The sunlight filters through the trees.")
            print("You see a path leading to a hut and another leading to a river.")
            print("Options:")
            print("(1) Go to the hut")
            print("(2) Follow the path to the river")
            print("(3) Check inventory")
            print("(4) Return to the cave")
            
            action = input("Choose an option: ")
            if action == "1":
                current_location = "hut"
            elif action == "2":
                current_location = "river"
            elif action == "3":
                check_inventory(inventory)
            elif action == "4":
                current_location = "cave"
            else:
                print("Invalid choice. Try again.")

        # Current Location: Hut
        elif current_location == "hut":
            print("\nYou arrive at a small, abandoned hut. Inside, you find an old chest.")
            print("Options:")
            print("(1) Open the chest")
            print("(2) Go back to the forest")
            
            action = input("Choose an option: ")
            if action == "1":
                if "key" not in inventory:
                    print("The chest is locked. You need a key.")
                else:
                    print("You use the key to open the chest and find a powerful healing potion!")
                    inventory.append("healing potion")
                    print("Healing potion added to inventory.")
            elif action == "2":
                current_location = "forest"
            else:
                print("Invalid choice. Try again.")

        # Current Location: River
        elif current_location == "river":
            print("\nYou reach a sparkling river. On the other side, you see the treasure glinting in the sunlight.")
            print("Options:")
            print("(1) Try to swim across")
            print("(2) Search for a bridge")
            print("(3) Go back to the forest")
            
            action = input("Choose an option: ")
            if action == "1":
                if "mysterious gem" in inventory:
                    print("The gem's power allows you to cross the river safely!")
                    print("Congratulations! You have reached the treasure and become the Lord of Doom!")
                    break
                else:
                    health -= 30
                    print(f"The current is too strong! You lose 30 health. Current health: {health}")
            elif action == "2":
                print("After some searching, you find a bridge a little upstream.")
                print("You cross the bridge just as it breaks beneath your feet. You reached the treasure! You've become the Lord of Doom!")
                break
            elif action == "3":
                current_location = "forest"
            else:
                print("Invalid choice. Try again.")
                
def check_inventory(inventory):
    if inventory:
        print("\nInventory:", ", ".join(inventory))
    else:
        print("\nYour inventory is empty.")
        
# Start the game
start_game()
