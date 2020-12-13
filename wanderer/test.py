from random import randrange
from area import Area
from hero import Hero
from skeleton import Skeleton
from boss import Boss
from game_manager import Game
from PIL import Image

test = Game()

characters = test.create_characters()
test.get_stats(characters)

hero = characters[0]
#hero.image_down.show()
hero.turn('left')
hero.image.show()

