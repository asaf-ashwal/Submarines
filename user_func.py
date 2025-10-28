from board import empty_board, secret_board


def get_game():
    while True:
        result = '3'
        # input('enter n the will be your board size, and your shots will be * 1.5: ')
        if result.isdigit():
            return {
                'display_board':empty_board(int(result)),
                'secret_board':secret_board(int(result)),
                'shots': int(int(result) * 1.5)
                }
print(get_game())