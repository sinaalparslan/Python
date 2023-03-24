from board import Board
from player import Player


def main():
    print('Menu'.center(50, '*'))
    x_player_name = input('first player name')
    o_player_name = input('second player')

    x_player = Player('X', x_player_name)
    o_player = Player('O', o_player_name)

    row_number = int(input('Row number'))
    column_number = int(input('Column number'))
    board = Board(row_number, column_number)
    count_num = 0

    while not board.is_game_ended():
        selected_move = int(input('choose youre move'))
        current_player = x_player if count_num % 2 == 0 else o_player
        is_board_changed = board.change_board(selected_move, current_player.act_sem)

        if is_board_changed == True:
            board.show_board()
            count_num += 1
        else:
            print('you have to choose another move')


main()
