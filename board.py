import random
def empty_board(squer_num):
    new_list = []
    for i in range(squer_num):
        tamp_list = []
        for j in range(squer_num):
            tamp_list.append('O')
        new_list.append(tamp_list)
    return new_list



def secret_board(squer_num):
    new_list = []
    for i in range(squer_num):
        tamp_list = []
        random_int = random.randrange(0, squer_num)
        print(random_int)
        for j in range(squer_num):
            if j == int(random_int):
                tamp_list.append('🚢')
            else: tamp_list.append('O')
        new_list.append(tamp_list)
    return new_list




def board_update(game,condition,location):
    if condition:
        game['display_board'][location[0]][location[1]] = 'V'
        game['hits'] += 1
    else:   
        game['display_board'][location[0]][location[1]] = 'X'
        game['shots'] -= 1
    return game['display_board'] 
    
