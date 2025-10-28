from board import empty_board, secret_board, board_update
from placement import is_it_a_ship


def get_game():
    while True:
        result = '3'
        # input('enter n the will be your board size, and your shots will be * 1.5: ')
        if result.isdigit():
            return {
                'display_board':empty_board(int(result)),
                'secret_board':secret_board(int(result)),
                'shots' :int(int(result) * 1.5),
                'hits' :0
                }
# print(get_game())




def handle_user_choice(game,location):
    result = is_it_a_ship(location,game['secret_board'])
    board_update(game['display_board'],result,location)




def user_choic(game):
    while True:
        print(f'your board {game['display_board']}')
        user_y = input('enter Y location: ')
        user_x= input('enter x location: ')
        if user_y.isdigit() and user_x.isdigit():
            handle_user_choice(game,[int(user_y),int(user_x)])
            print(game['display_board'])
            # print([user_x,user_y])
            return True
        
        
# user_choic({'display_board': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 'secret_board': [['O', 'O', '🚢'], ['O', '🚢', 'O'], ['O', 'O', '🚢']], 'shots': 4})