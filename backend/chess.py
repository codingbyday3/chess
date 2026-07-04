import chess_pieces


board = [
    ['2r', '2n', '2b', '1q', '2k', '2b', '2n', '2r'],
    ['2p', '2p', '2p', '2p', '2p', '2p', '2p', '2p',],
    ['', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', ],
    ['1p', '1p', '1p', '1p', '1p', '1p', '1p', '1p',],
    ['1r', '1n', '1b', '1q', '1k', '1b', '1n', '1r'],
]

board_marks = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    '1': 8,
    '2': 7,
    '3': 6,
    '4': 5,
    '5': 4,
    '6': 3,
    '7': 2,
    '8': 1
}

white_king = 'e1'
black_king = 'e8'
is_check = False

is_game_ended = False



def main():
    play_game()

def play_game():

    global board
    global is_check

    player_on_move = '1'
    while not is_game_ended:
        figure = input('what figure will you move: ')
        old_position = input('From where: ')
        new_position = input('Where do you want to move this figure: ')

        if not are_moves_valid(player_on_move, old_position, new_position, figure):
            print('This move is not allowed')
            print(output_editor(board))

            continue 


        change_position(old_position, new_position, figure)

        if player_on_move == '1':
            is_check = not are_moves_valid(player_on_move, new_position, black_king, figure)
            player_on_move = '2'
        else:
            is_check = not are_moves_valid(player_on_move, new_position, white_king, figure)
            player_on_move = '1'
    
        if is_check:
            print('Check')

def change_position(old_position, new_position, figure):
    global board

    board[board_marks[old_position[1]] - 1 ][board_marks[old_position[0]] - 1] = ''
    board[board_marks[new_position[1]] - 1][board_marks[new_position[0]] - 1] = figure
    print(output_editor(board))

def are_moves_valid(player, old_position, new_position, figure):

    if len(old_position) != 2 or len(new_position) != 2:
        return False
    
    figure_player = figure[0]
    figure_name = figure[1]
    if is_check and figure != 'k':
        return False

    if player != figure_player:
        return False
    elif figure_name == 'p':
        pawn_rules = chess_pieces.Pawn(figure_player, board, board_marks[old_position[0]] - 1, board_marks[old_position[1]] - 1 )
        if not pawn_rules.valid_moves(board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1):
            return False
    elif figure_name == 'n':
        knight_rules = chess_pieces.Knight(figure_player, board, board_marks[old_position[0]] - 1, board_marks[old_position[1]] - 1 )
        if not knight_rules.valid_moves(board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1):
            return False
    elif figure_name == 'b':
        bishop_rules = chess_pieces.Bishop(figure_player, board, board_marks[old_position[0]] - 1, board_marks[old_position[1]] - 1 )
        if not bishop_rules.valid_moves(board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1):
            return False
    elif figure_name == 'r':
        rook_rules = chess_pieces.Rook(figure_player, board, board_marks[old_position[0]] - 1, board_marks[old_position[1]] - 1 )
        if not rook_rules.valid_moves(board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1):
            return False
    elif figure_name == 'q':
        queen_rules = chess_pieces.Queen(figure_player, board, board_marks[old_position[0]] - 1, board_marks[old_position[1]] - 1 )
        if not queen_rules.valid_moves(board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1):
            return False
    elif figure_name == 'k':

        global white_king
        global black_king

        king_rules = chess_pieces.King(figure_player, board, board_marks[old_position[0]] - 1, board_marks[old_position[1]] - 1 )

        if not king_rules.valid_moves(board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1):
            return False
        
        if figure_player == 1:
            white_king = (board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1)
        elif figure_player == 2:
            black_king = (board_marks[new_position[0]] - 1, board_marks[new_position[1]] - 1)
            
    return True


def is_check_mate(king_position):
    pass

def output_editor(table):
    for line in table:
        print(f'{line}\n')


main()

