from hero import Hero
from skeleton import Skeleton
from boss import Boss
from game_manager import GameManager
from PIL import Image, ImageTk
from tiles import Floor, Wall
from pynput.keyboard import Key, Listener
from area import Area
from tkinter import *

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("Wanderer by Mark Ambrus")
        self.area = Area()
        self.game_manager = GameManager()
        self.hero = Hero()

        self.size = self.area.size
        self.height = self.area.size + 50
        self.canvas = Canvas(self.root, width=self.size, height=self.size)
        self.canvas.pack()
        self.area.draw_map(self.canvas)

        self.characters = self.game_manager.create_characters(self.hero)
        self.monsters = self.characters[1:]

        self.label = Label(text=self.hero.introduce())
        self.label.pack()

        self.game_manager.spawn_characters(self.area, self.canvas, self.characters)
        #self.game_manager.get_stats(self.characters)

        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()

        self.root.mainloop()

    def on_key_press(self, e):
        #global direction
        #NOTE use dictionary as switch?
        if e.keycode == 87 or e.keycode == 119 or e.keycode == 8320768: #W w up
            direction = 'up'
        elif e.keycode == 83 or e.keycode == 115 or e.keycode == 8255233: #S s down
            direction = 'down'
        elif e.keycode == 65 or e.keycode == 97 or e.keycode == 8124162: #A a left
            direction = 'left'
        elif e.keycode == 68 or e.keycode == 100 or e.keycode == 8189699: #D d right
            direction = 'right'
        #elif e.keycode == 3473435: exit game
        else:
            print('Use the arrow keys or WASD to move')
            return
        self.game_turn(direction)

    def game_turn(self, direction):
        self.game_manager.set_hero_position(self.area, self.canvas, self.hero, direction, self.monsters)
        #game_manager.check_next_area(area, canvas, characters)

print("Welcome to the Wanderer game! Let's play!")
print("Use the arrow keys or WASD to move the hero.")
print("Cross path with monsters to fight them.")
print("Collect the key and kill the boss to get to the next level.")
app = App()
