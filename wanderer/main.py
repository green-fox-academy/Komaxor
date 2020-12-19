from area import CreateArea
from game_manager import Game
from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'w':
            game_manager.set_character_position(hero, 'up')
        if key.char == 's':
            game_manager.set_character_position(hero, 'down')
        if key.char == 'a':
            game_manager.set_character_position(hero, 'left')
        if key.char == 'd':
            game_manager.set_character_position(hero, 'right')
    except AttributeError:
        pass

def on_release(key):
    pass

while True: #app
    #print('the app started')
    print("Mark: Welcome to the Wanderer game! Let's play!")
    game_manager = Game()

    while True: #game
        print('the game started')
        characters = game_manager.create_characters()
        hero = characters[0]
        monsters = characters[1:]
        boss = characters[1]
        skeletons = characters[2:]
        directions = ['up', 'down', 'left', 'right']
        game_manager.get_stats(characters)

        area = CreateArea()
        area.draw_map()

        while True: #area
            #print('the area started')
            turn = 1
            game_manager.spawn_characters(area, hero, monsters)
            area.display()
            with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as l:
                l.join()
            #game_manager.move(hero, direction)
            game_manager.check_next_area(area, characters)
            if turn % 2 == 0:
                for monster in monsters:
                    game_manager.set_character_position(monsters, directions[0]) #choose randomly
            game_manager.check_next_area(area, characters)
            turn += 1


'''
    restart = str(input("Play again? "))
    if restart.lower().startswith("y"):
        continue
    else:
        print("Bye")
        break
'''