from phrasehunter.game import Game

if __name__ == '__main__':
    replay = True
    while replay:
        game = Game()
        game.start()
        replay = game.start_over()
    print('Thank you for playing! Closing game...')
    exit()

