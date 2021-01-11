# Wanderer by Mark Ambrus

## Project structure:
The project folder includes all relevant files for the project.
There are 11 .py scripts and the assets folder that contains 8 .gif images.
2 of those are for the two types of tiles, 4 for the hero and 2 for the two
types of monsters.

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
3. Use the arrow keys or WASD to move the hero around
4. Close the application window once finished.

## Code structure:

The app contains the following classes:
App
GameManager
Area
Tile
    Floor
    Wall
Character
    Hero
    Monster
        Boss
        Skeleton


In main.py there is the App class. It initialises the game and includes the
mainloop. The program starts by creating the app object.
To visualize the app tkinter is used. The application window is created. The
game_manager object is created, based on which the game area, the characters
and all labels are packed inside. The program is listening for key inputs, upon
relevant input, it returns the direction. The game_turn function is executed
that triggers a series of events based on the underlying factors.

In game_manager.py there is the GameManager class. It manages most of the game
logic. It creates the characters and the area. It also keeps count of the
current area and the kill count.

The area.py defines the size of the game area, the position of the walls and
floors, keeps track of the turns, the occupancy of the tiles and the images of
the living characters. It has methods for creating a map, displaying the map on
the canvas and displaying a character on the canvas.

The tiles.py contains the common Tile class.
 and its 2 children, Wall and Floor.
It stores whether the given tile can be occupied by a character and whether a
monster or the hero occupies it. It also defines the source of the image of the
tiles.

character.py has the attributes and methods that are common for the characters.
hero.py and monster.py are children of character.py.
hero.py contains attributes and methods specific to the hero.
boss.py and skeleton.py and children of monster.py
boss.py and skeleton.py contains the Boss and Skeleton classes respectively.