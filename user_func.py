from board import empty_board, secret_board, board_update
from placement import is_it_a_ship


def get_game():
    while True:
        result = input('enter n the will be your board size, and your shots will be * 1.5: ')
        if result.isdigit():
            return {
                'display_board':empty_board(int(result)),
                'secret_board':secret_board(int(result)),
                'shots' :round(int(result) * 1.5),
                'hits' :0
                }




def handle_user_choice(game,location):
    result = is_it_a_ship(location,game['secret_board'])
    board_update(game,result,location)




def user_choic(game):
    while True:
        print(f'your board {game['display_board']}')
        user_y = input('enter Y location: ')
        if not(len(user_y) == 1) or not(user_y.isdigit()):
            print('enter one int on y')
            continue
        user_x= input('enter x location: ')
        if not(len(user_x) == 1) or not(user_x.isdigit()):
            print('enter one int on x')
            continue
        if game['display_board'][int(user_y)][int(user_x)] != 'O':
            print('you all ready gest that')
        handle_user_choice(game,[int(user_y),int(user_x)])
        return True
        
        
