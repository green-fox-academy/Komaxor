from game_manager import GameManager
from pynput.keyboard import Key, Listener
from tkinter import Tk, Canvas, Label

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("Wanderer by Mark Ambrus")
        self.game_manager = GameManager()

        self.size = self.game_manager.area.size
        self.canvas = Canvas(self.root, width=self.size, height=self.size)
        self.canvas.pack()
        self.game_manager.area.draw_map(self.canvas)

        self.hero_stat_bar = Label(text=self.game_manager.hero.introduce())
        self.hero_stat_bar.pack()
        #NOTE how to break lines below
        self.game_description = Label(text="Welcome to the Wanderer game! Let's play! Use the arrow keys or WASD to move the hero.\n Cross path with monsters to fight them. Collect the key and kill the boss to get to the next level.")
        self.game_description.pack()

        self.progress_info = Label(text="Area: " +
                                str(self.game_manager.area_number) + " | " +
                                str(self.game_manager.kill_count) +
                                " monsters slayed.")
        self.progress_info.pack()

        self.game_manager.spawn_characters(self.canvas)
        #self.game_manager.get_stats()

        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()

        self.root.mainloop()

    def on_key_press(self, e):
        #global direction #NOTE global or local and pass?
        #NOTE use dictionary as switch?
        #W or w or up arrow key
        if e.keycode == 87 or e.keycode == 119 or e.keycode == 8320768:
            direction = 'up'
        #S or s or down arrow key
        elif e.keycode == 83 or e.keycode == 115 or e.keycode == 8255233:
            direction = 'down'
        #A or a or left arrow key
        elif e.keycode == 65 or e.keycode == 97 or e.keycode == 8124162:
            direction = 'left'
        #D or d or right arrow key
        elif e.keycode == 68 or e.keycode == 100 or e.keycode == 8189699:
            direction = 'right'
        #space key
        #elif e.keycode == 32: #NOTE when to fight?
            #self.game_manager.fight(hero, monster_in_place new logic)
        else:
            #print('Use the arrow keys or WASD to move and space to fight')
            return
        self.game_turn(direction)

    def game_turn(self, direction):
        self.game_manager.set_hero_position(self.canvas, direction)
        if self.game_manager.hero.current_health <= 0:
            print('Game Over')
            self.game_manager = GameManager()
            self.game_manager.area.draw_map(self.canvas)
            self.game_manager.spawn_characters(self.canvas)
            self.config_labels()
            return
        self.game_manager.check_next_area(self.canvas)
        self.config_labels()

    def config_labels(self):
        self.progress_info.config(text="Area: " +
                str(self.game_manager.area_number) + " | " +
                str(self.game_manager.kill_count) +
                " monsters slayed.")
        self.hero_stat_bar.config(text=self.game_manager.hero.introduce())

app = App()
