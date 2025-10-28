import random
def empty_board(squer_num):
    new_list = []
    for i in range(squer_num):
        tamp_list = []
        for j in range(squer_num):
            tamp_list.append('O')
        new_list.append(tamp_list)
    return new_list

# print(empty_board(4))

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