from hero import Hero
from skeleton import Skeleton
from boss import Boss
from game_manager import Game
from PIL import Image, ImageTk
from tiles import Floor, Wall
from pynput.keyboard import Key, Listener
from area2 import Area
from tkinter import *

def on_key_press(self, e):
    if e.keycode == 87:   # W
        return' up'
    elif e.keycode == 83:  # S
        return 'down'
    elif e.keycode == 65:  # A
        return 'left'
    elif e.keycode == 68:  # D
        return 'right'

def on_release(key):
    pass

game_manager = Game()

characters = game_manager.create_characters()
hero = characters[0]
monsters = characters[1:]
boss = characters[1]
skeletons = characters[2:]

area = Area()
wall = Wall()

# Create the tk environment as usual
root = Tk()
canvas = Canvas(root, width=area.app_x, height=area.app_y)
canvas.pack()
area.draw(canvas)
root.mainloop()

#canvas.bind("<KeyPress>", on_key_press)
#canvas.focus_set()

# Draw the box in the initial position
#area.draw(canvas)
'''
game_manager.spawn_characters(area, hero, monsters)

game_manager.move(hero, 'right')
game_manager.move(hero, 'right')
game_manager.move(hero, 'right')
#area.display()

hero.image.show()
hero.turn('left')
hero.image.show()

print(game_manager.get_stats(characters))
game_manager.fight(hero, boss)
print(game_manager.get_stats(characters))

with Listener(
    on_press=on_press,
    on_release=on_release) as l:
    l.join()
    '''
