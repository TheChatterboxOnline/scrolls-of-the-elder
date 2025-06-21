# Elder Scrolls: A Text-Based RPG

Welcome to a text-based adventure set in the world of The Elder Scrolls IV: Oblivion! This is a simple, expandable RPG framework written in Python. You begin your journey, as all heroes of Cyrodiil do, in the Imperial Prison.

![Oblivion Logo](https://upload.wikimedia.org/wikipedia/en/2/21/The_Elder_Scrolls_IV_Oblivion_cover.png)

## Features

-   **Classic RPG Mechanics:** Create a character, choosing from classic Oblivion races and classes.
-   **Stat System:** Your character has attributes (Strength, Intelligence, etc.) and skills (Blade, Destruction, etc.) that are affected by your choices.
-   **Interactive World:** Move between locations, examine your surroundings, and pick up items.
-   **Expandable by Design:** The entire game world is built using simple Python dictionaries, making it incredibly easy to add new locations, items, and events.

## How to Run the Game

1.  Make sure you have **Python 3** installed on your system.
2.  Clone or download this repository.
3.  Navigate to the project directory in your terminal.
4.  Run the game with the following command:

    ```bash
    python game.py
    ```

5.  Follow the on-screen prompts to create your character and begin your adventure!

## How to Play

The game is controlled by simple text commands. Here are the basics:

-   `look` or `l`: Get a description of your current location.
-   `move` or `go`: Travel to a connected location.
-   `take [item name]`: Pick up an item you see in the room.
-   `inventory` or `i`: Check what you're carrying.
-   `stats`: View your character sheet.
-   `search [target]`: Investigate something more closely (e.g., `search goblin`).
-   `help`: Shows the list of available commands.
-   `quit`: Exits the game.

## How to Expand the Game (For Developers)

This project is designed to be a starting point. Here’s how you can add your own content directly in `game.py`:

### Adding a New Location

To add a new location, simply add a new entry to the `LOCATIONS` dictionary. Follow the existing format:

```python
'market': {
    'name': 'Market District',
    'description': "The bustling heart of commerce in the city. Merchants hawk their wares and the air is filled with the smells of fresh bread and steel.",
    'connections': {'talos': 'Talos Plaza District', 'arena': 'The Arena'},
    'items': ['Flagon of Ale', 'Apple'],
    'events': {}
},
# Don't forget to add a connection from another location to your new one!
# For example, in the 'talos' location:
# 'connections': {'waterfront': '...', 'market': 'Market District'},
```

### Adding NPCs and Quests

You can add an `npcs` key to a location's dictionary and create a simple `talk` command in the main game loop to interact with them, triggering quests and dialogue.

### Creating a Combat System

You could implement a `fight` command that initiates a turn-based combat loop with an enemy (which could also be defined in the location data). The outcome would be determined by comparing player and enemy stats.

This is your world now. Build it out! Add the Dark Brotherhood sanctuary, the Mages Guild, the wilderness of Cyrodiil—the possibilities are endless.
