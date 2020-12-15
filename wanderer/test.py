from random import randrange
from area import CreateArea
from hero import Hero
from skeleton import Skeleton
from boss import Boss
from game_manager import Game
from PIL import Image
from tiles import Floor, Wall

game_manager = Game()

characters = game_manager.create_characters()
hero = characters[0]
monsters = characters[1:]
boss = characters[1]
skeletons = characters[2:]
game_manager.get_stats(characters)

area = CreateArea()
area.draw_map()
game_manager.spawn_characters(area, hero, monsters)
area.display()

'''
hero.image.show()
hero.turn('left')
hero.image.show()
'''