# Wanderer by Mark Ambrus

## File structure:
The project consists of 17 files in the project folder.
8 of those are .gif images and 9 are .py program files.

## Required to launch:
1. Have the repository cloned to your device.
2. Have Pthon 3.x installed on your device.
The program was written in python3.9.0 and is meant to be used with Python 3.x.

## How to use:
1. Open the terminal and navigate inside the directory.
2. Type "python3 main.py" to start the app.
```bash
python3 main.py
```

## Code structure:
To visualize the app tkinter is used.
main.py includes the mainloop and all necessary imports and methods.
game_manager.py manages the area and the characters.
area.py deals with visualization.
tiles.py contains the common Tile class and its 2 children, Wall and Floor.
The 8 .gif images of the tiles and the characters are in the assets folder.
character.py has the attributes and methods that are common for the characters.
hero.py and monster.py are children of character.py.
hero.py contains attributes and methods specific to the hero.
boss.py and skeleton.py and children of monster.py