winning_combinations = [{0, 1, 2}, {0, 3, 6}, {0, 4, 8}, {1, 4, 7}, {2, 5, 8}, {2, 4, 6}, {3, 4, 5}, {6, 7, 8}]
def draw_play(x_moves, o_moves, play_ground):
    print('-'*15)
    play_sentence = []
    for i in range(9):
        if i in x_moves:
            play_sentence.append(' X ')
        elif i in o_moves:
            play_sentence.append(' O ')
        elif i in play_ground:
            play_sentence.append(f' {i} ')

    for i in [3,6,9]:
        for char in play_sentence[i-3:i]:
            print(f"|{char}",end='')
        print("|")
        print('-' * 15)

def check_winner(player_list):
    for w in winning_combinations:
        if w.issubset(player_list):
            return True
    return False

def get_move(player_name, player, moves):
    while True:
        try:
            move = int(input(f'{player_name} turn: '))
            if move not in moves:
                print("not allowed move")
                continue
            player.add(move)
            moves.remove(move)
            return
        except ValueError:
            print("not allowed")



def game():
    x_player = set()
    o_player = set()
    available_moves = set(range(9))
    draw_play(x_player, o_player, available_moves)
    while True:
        if len(available_moves) == 0:
            print("DRAW!")
            break
        get_move("X",x_player, available_moves)
        draw_play(x_player, o_player, available_moves)
        if check_winner(x_player):
            print('congrats X')
            break
            
        if len(available_moves) == 0:
            print("DRAW")
            break
        get_move("O",o_player, available_moves)
        draw_play(x_player, o_player, available_moves)
        if check_winner(o_player):
            print('congrats o')
            break

game()
while True:
    q = input("Do you want to play again?(press y)")
    if q == 'y':
        game()
    else:
        break
