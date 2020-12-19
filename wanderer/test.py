from hero import Hero
from skeleton import Skeleton
from boss import Boss
from game_manager import Game
from PIL import Image, ImageTk
from tiles import Floor, Wall
from pynput.keyboard import Key, Listener
from area2 import Area
from tkinter import *

def on_key_press(e):
    global direction
    if e.keycode == 87 or e.keycode == 119 or e.keycode == 8320768: # W and w and up arrow
        direction = 'up'
    elif e.keycode == 83 or e.keycode == 115 or e.keycode == 8255233: # S and s and down arrow
        direction = 'down'
    elif e.keycode == 65 or e.keycode == 97 or e.keycode == 8124162: # A and a and left arrow
        direction = 'left'
    elif e.keycode == 68 or e.keycode == 100 or e.keycode == 8189699: # D and d and right arrow
        direction = 'right'
    #elif e.keycode == 3473435: exit game
    game_turn()

def on_release(e):
    pass

def game_turn():
    game_manager.set_hero_position(area, canvas, hero, direction)
    #game_manager.check_next_area(area, canvas, characters)
    if game_manager.turn_count % 2 == 0:
        for monster in monsters:
            game_manager.set_monster_position(area, canvas, monster)
    for tile in area.tiles.keys():
        if tile not in area.free_tiles[0]:
            print(tile)
    print(game_manager.turn_count)

game_manager = Game()

characters = game_manager.create_characters()
hero = characters[0]
monsters = characters[1:]
#boss = characters[1]
#skeletons = characters[2:]

area = Area()

# Create the tk environment as usual
root = Tk()
canvas = Canvas(root, width=area.app_x, height=area.app_y)
canvas.pack()
area.draw_map(canvas)
game_manager.spawn_characters(area, canvas, characters)
game_manager.get_stats(characters)

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

root.mainloop()
'''

print(game_manager.get_stats(characters))
game_manager.fight(hero, boss)
print(game_manager.get_stats(characters))
    '''
