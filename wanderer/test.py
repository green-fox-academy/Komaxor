from random import randrange
from area import CreateArea
from hero import Hero
from skeleton import Skeleton
from boss import Boss
from game_manager import Game
from PIL import Image
from tiles import Floor, Wall
from pynput.keyboard import Key, Listener

def on_press(key):
    #keys = ['w', 's', 'a', 'd']
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        if key.char == 'w':
            game_manager.move(hero, 'up')
        if key.char == 's':
            game_manager.move(hero, 'down')
        if key.char == 'a':
            game_manager.move(hero, 'left')
        if key.char == 'd':
            game_manager.move(hero, 'right')
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        pass

def on_release(key):
    pass

game_manager = Game()

characters = game_manager.create_characters()
hero = characters[0]
monsters = characters[1:]
boss = characters[1]
skeletons = characters[2:]

area = CreateArea()
area.draw_map()
game_manager.spawn_characters(area, hero, monsters)
#area.display()
'''
hero.image.show()
hero.turn('left')
hero.image.show()
'''

print(game_manager.get_stats(characters))
game_manager.fight(hero, boss)
print(game_manager.get_stats(characters))


with Listener(
    on_press=on_press,
    on_release=on_release) as l:
    l.join()