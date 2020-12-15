from area import CreateArea
from game_manager import Game

while True: #app
    #print('the app started')
    print("Mark: Welcome to the Tic-Tac-Toe game! Let's play!")
    game_manager = Game()

    while True: #game
        #print('the game started')
        characters = game_manager.create_characters()
        hero = characters[0]
        monsters = characters[1:]
        boss = characters[1]
        skeletons = characters[2:]
        game_manager.get_stats(characters)

        area = CreateArea()
        area.draw_map()

        while True: #area
            #print('the area started')
            turn = 1
            game_manager.spawn_characters(area, hero, monsters)
            area.display()
            direction = game_manager.player_input()
            game_manager.move(hero, direction)
            game_manager.check_next_area(area, characters)
            if turn % 2 == 0:
                for monster in monsters:
                    game_manager.move(monsters, direction)
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