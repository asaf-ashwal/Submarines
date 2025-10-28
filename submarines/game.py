from submarines.user_func import get_game, user_choic
from submarines.placement import won

def init_game():
    game = get_game()
    while True:
        print('shots: ',game['shots'])
        user_choic(game)
        if won(game):
            print('!!!   wonnnnn   !!!')
            break
        elif game['shots'] == 0:
            print("You're out of ammunition.")
            break
