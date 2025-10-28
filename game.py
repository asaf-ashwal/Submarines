from user_func import get_game, user_choic
from placement import won

def init_game():
    game = get_game()
    while True:
        user_choic(game)
        if won():
            print('won')
            break
            print('out of ammo')
        elif game['shots'] == 0:
