import time
import textwrap
import sys

# A simple "typewriter" effect for displaying text
def type_text(text, speed=0.04):
    for char in textwrap.fill(text, 70):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class Player:
    def __init__(self, name, race, p_class):
        self.name = name
        self.race = race
        self.p_class = p_class
        self.location = 'imperial_prison'
        self.health = 100
        self.magicka = 100
        self.fatigue = 120
        self.inventory = ['Prison Rags', 'Prison Key']
        self.attributes = {
            'Strength': 40,
            'Intelligence': 40,
            'Willpower': 40,
            'Agility': 40,
            'Speed': 40,
            'Endurance': 40,
            'Personality': 40,
            'Luck': 50
        }
        self.skills = {
            'Blade': 5,
            'Blunt': 5,
            'Hand to Hand': 5,
            'Armorer': 5,
            'Block': 5,
            'Heavy Armor': 5,
            'Athletics': 5,
            'Acrobatics': 5,
            'Light Armor': 5,
            'Security': 5,
            'Sneak': 5,
            'Marksman': 5,
            'Mercantile': 5,
            'Speechcraft': 5,
            'Illusion': 5,
            'Alchemy': 5,
            'Conjuration': 5,
            'Destruction': 5,
            'Mysticism': 5,
            'Alteration': 5,
            'Restoration': 5
        }
        self.apply_race_bonuses()
        self.apply_class_bonuses()

    def apply_race_bonuses(self):
        # Simplified race bonuses
        if self.race.lower() == 'imperial':
            self.attributes['Personality'] += 10
            self.skills['Speechcraft'] += 10
        elif self.race.lower() == 'nord':
            self.attributes['Strength'] += 10
            self.skills['Blunt'] += 10
        elif self.race.lower() == 'dunmer': # Dark Elf
            self.attributes['Speed'] += 10
            self.skills['Destruction'] += 10
        # Add other races here...

    def apply_class_bonuses(self):
        # Simplified class bonuses
        if self.p_class.lower() == 'warrior':
            self.skills['Blade'] += 10
            self.skills['Block'] += 10
            self.skills['Heavy Armor'] += 10
        elif self.p_class.lower() == 'mage':
            self.skills['Destruction'] += 10
            self.skills['Alteration'] += 10
            self.skills['Mysticism'] += 10
        elif self.p_class.lower() == 'thief':
            self.skills['Sneak'] += 10
            self.skills['Security'] += 10
            self.skills['Light Armor'] += 10
        # Add other classes here...

    def show_stats(self):
        print("\n--- CHARACTER STATS ---")
        print(f"Name: {self.name}")
        print(f"Race: {self.race.capitalize()}, Class: {self.p_class.capitalize()}")
        print(f"Health: {self.health}, Magicka: {self.magicka}")
        print("\n--- Attributes ---")
        for attr, value in self.attributes.items():
            print(f"{attr}: {value}")
        print("\n--- Skills ---")
        for skill, value in self.skills.items():
            print(f"{skill}: {value}")
        print("-----------------------\n")

    def show_inventory(self):
        print("\n--- INVENTORY ---")
        if not self.inventory:
            print("You are carrying nothing.")
        else:
            for item in self.inventory:
                print(f"- {item}")
        print("-------------------\n")

# --- Game Data ---
# Using dictionaries to store game world data. Easy to expand!
LOCATIONS = {
    'imperial_prison': {
        'name': 'Imperial Prison Cell',
        'description': "You are in a dark, damp prison cell. The stone walls are cold to the touch. A single torch flickers outside your cell, casting long shadows. A locked gate is your only exit, but a dead goblin lies in the corner, clutching a key.",
        'connections': {'sewers': 'Imperial Subterrane'},
        'items': [],
        'events': {'search goblin': "You find a 'Prison Key' on the goblin's body."}
    },
    'sewers': {
        'name': 'Imperial Subterrane',
        'description': "You've unlocked the gate and entered a foul-smelling sewer. Tunnels stretch into the darkness. You hear the skittering of rats. A wooden door leads to the waterfront, and a ladder leads up to the city streets.",
        'connections': {'waterfront': 'Imperial City Waterfront', 'streets': 'Talos Plaza District'},
        'items': ['Rusty Iron Dagger'],
        'events': {}
    },
    'waterfront': {
        'name': 'Imperial City Waterfront',
        'description': "You emerge into the salty air of the Waterfront. It's a rough-and-tumble district of warehouses and rickety shacks. The Imperial City's grand walls tower above you.",
        'connections': {'sewers': 'Imperial Subterrane', 'talos': 'Talos Plaza District'},
        'items': [],
        'events': {}
    },
    'talos': {
        'name': 'Talos Plaza District',
        'description': "This is the heart of the Imperial City. Grand statues, beautiful homes, and paved streets are a far cry from the prison. People walk by, going about their day. You feel a sense of freedom, and opportunity.",
        'connections': {'waterfront': 'Imperial City Waterfront', 'market': 'Market District'},
        'items': [],
        'events': {}
    },
    # Add more locations here...
}

def character_creation():
    type_text("You awaken in a cold, dark cell. You don't know how you got here.")
    time.sleep(1)
    type_text("A voice from the next cell calls out, 'You're finally awake... Who are you?'")
    
    name = input("> What is your name? ")
    
    type_text(f"'Ah, {name}. A fine name. And what about your people? Are you a hardy Nord, a noble Imperial, or perhaps a cunning Dunmer?'")
    race = ""
    while race.lower() not in ['nord', 'imperial', 'dunmer']:
        race = input("> Choose your race (Nord, Imperial, Dunmer): ")
        if race.lower() not in ['nord', 'imperial', 'dunmer']:
            type_text("I've not heard of such a race. Try again.")

    type_text("'I see. And what is your trade? A Warrior, swinging a heavy blade? A Mage, weaving powerful spells? Or a Thief, who walks in the shadows?'")
    p_class = ""
    while p_class.lower() not in ['warrior', 'mage', 'thief']:
        p_class = input("> Choose your class (Warrior, Mage, Thief): ")
        if p_class.lower() not in ['warrior', 'mage', 'thief']:
            type_text("That's no profession I recognize. Stick to the common trades.")

    return Player(name, race, p_class)

def game_loop(player):
    while True:
        current_loc_key = player.location
        current_location = LOCATIONS[current_loc_key]

        print("\n" + "="*30)
        type_text(current_location['name'], 0.02)
        print("="*30)
        time.sleep(0.5)
        type_text(current_location['description'])
        
        # Display items in the location
        if current_location['items']:
            print("\nYou see here: " + ", ".join(current_location['items']))

        # Get player command
        command_input = input("\n> What do you do? ").lower().strip()
        command_parts = command_input.split()
        verb = command_parts[0] if command_parts else ""

        # --- Process Commands ---
        if verb == "quit":
            type_text("You have left the world of Cyrodiil. Farewell.")
            break
        elif verb in ["look", "l"]:
            continue # The location description is already printed at the start of the loop
        elif verb in ["stats", "attributes", "skills"]:
            player.show_stats()
        elif verb in ["inventory", "i", "inv"]:
            player.show_inventory()
        elif verb in ["move", "go"]:
            print("Where do you want to go?")
            for dest_key, dest_name in current_location['connections'].items():
                print(f"- {dest_key}")
            
            dest_choice = input("> ")
            if dest_choice in current_location['connections']:
                player.location = dest_choice
                type_text(f"You travel to the {LOCATIONS[player.location]['name']}...")
            else:
                print("You can't go that way.")
        elif verb in ["take", "get", "grab"]:
            if len(command_parts) > 1:
                item_name = " ".join(command_parts[1:]).title() # Handle multi-word items
                if item_name in current_location['items']:
                    player.inventory.append(item_name)
                    current_location['items'].remove(item_name)
                    type_text(f"You picked up the {item_name}.")
                else:
                    print("That item is not here.")
            else:
                print("What do you want to take?")
        elif verb in ["search", "check"]:
             # Simple event handling
            if 'search goblin' in command_input and 'search goblin' in current_location.get('events', {}):
                type_text(current_location['events']['search goblin'])
                if 'Prison Key' not in player.inventory:
                    player.inventory.append('Prison Key')
                current_location['events'].pop('search goblin') # Event only happens once
            else:
                print("You find nothing of interest.")
        elif verb in ["help", "?"]:
            print("\n--- Available Commands ---")
            print("look (l): Examine your surroundings.")
            print("move/go: Travel to a new location.")
            print("take [item]: Pick up an item.")
            print("inventory (i/inv): Check your belongings.")
            print("stats: Check your character attributes and skills.")
            print("search [target]: Look for things on a target.")
            print("quit: Exit the game.")
            print("------------------------\n")
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")


if __name__ == "__main__":
    player = character_creation()
    type_text(f"\nWelcome to Cyrodiil, {player.name}. Your journey begins now.")
    player.show_stats()
    input("Press Enter to continue...")
    game_loop(player)