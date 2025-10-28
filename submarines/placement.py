
def is_it_a_ship(location,board):
    return board[location[0]][location[1]] == '🚢'


def won(game):
    return game['hits'] == round(len(game['secret_board'])) 