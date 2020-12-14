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

floor = Floor()
wall = Wall()
tile_size = floor.image.size[0]
num_tiles = 10
area = CreateArea(tile_size, (tile_size * num_tiles))
area.get_walls()
for i in range(num_tiles ** 2):
    if area.tiles.get(i) == "Wall":
        image = wall.image
    elif area.tiles.get(i) == "Floor":
        image = floor.image
    area.paste_image(image)
game_manager.spawn_characters(area, hero, monsters)
area.show()

'''
hero.image.show()
hero.turn('left')
hero.image.show()

'''