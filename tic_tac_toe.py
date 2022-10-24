def player_setup():
    player_one = input(f"Player one name:\n")
    player_two = input(f"Player two name:\n")

    while player_two == player_one:
        player_two = input(f"Player name already taken, please choose another:\n")

    def get_players_symbol():
        symbol = input(f"{player_one} would you like to play with 'X' or 'O'?\n").upper()
        while symbol not in ["X", "O"]:
            symbol = input("Please, choose valid symbol: 'X' or 'O'\n")

        if symbol == 'X':
            return 'X', 'O'
        return 'O', 'X'

    pl_1, pl_2 = get_players_symbol()

    players = {
        player_one: pl_1,
        player_two: pl_2,
    }

    return players


def get_player_choice(player, positions):
    def validate_player_choice(choice):
        try:
            if int(choice) not in positions:
                return False
        except:
            return False
        return True

    player_choice = input(f"{player} choose a free position [1-9]:\n")
    while not validate_player_choice(player_choice):
        player_choice = input(f"Choose a valid position.\n")
    return int(player_choice)


def apply_player_choice(board, choice, available_positions, current_symbol):
    r, c = available_positions[choice]
    board[r][c] = current_symbol
    available_positions.pop(choice)
    return r, c


def create_board():
    board = []
    for n in range(3):
        row = [" "] * 3
        board.append(row)

    return board


def print_board(board):
    # def get_value(value):
    #     if value is None:
    #         return " "
    #     else:
    #         return value

    for x in board:
        print(f"| {' | '.join(x)} |")


def create_dummy_board():
    i = 1
    board = []
    for n in range(3):
        row = []
        for j in range(3):
            row.append(str(i))
            i += 1
        board.append(row)

    return board


def check_win_condition(board, row, col, current_symbol):
    win_condition = [current_symbol] * len(board)

    def get_right_path():
        path = []
        for c in range(col, len(board)):
            path.append(board[row][c])
        return path

    def get_left_path():
        path = []
        for c in range(col, -1, -1):
            path.append(board[row][c])
        return path

    def get_up_path():
        path = []
        for r in range(row, -1, -1):
            path.append(board[r][col])
        return path

    def get_down_path():
        path = []
        for r in range(row, len(board)):
            path.append(board[r][col])
        return path

    def get_left_up_diagonal():
        path = []
        i = col
        for r in range(row, -1, -1):
            try:
                if row < 0 or i < 0:
                    break
                path.append(board[r][i])
                i -= 1
            except IndexError:
                break

        return path

    def get_right_up_diagonal():
        path = []
        i = col
        for r in range(row, -1, -1):
            try:
                if row < 0 or i < 0:
                    break
                path.append(board[r][i])
                i += 1
            except IndexError:
                break

        return path

    def get_right_down_diagonal():
        path = []
        i = col
        for r in range(row, len(board)):
            try:
                path.append(board[r][i])
                i += 1
            except IndexError:
                break

        return path

    def get_left_down_diagonal():
        path = []
        i = col
        for r in range(row, len(board)):
            try:
                if i < 0:
                    break
                path.append(board[r][i])
                i -= 1
            except IndexError:
                break

        return path

    right_path = get_right_path()
    left_path = get_left_path()
    up_path = get_up_path()
    down_path = get_down_path()
    left_up_diagonal = get_left_up_diagonal()
    right_up_diagonal = get_right_up_diagonal()
    right_down_diagonal = get_right_down_diagonal()
    left_down_diagonal = get_left_down_diagonal()


    paths = (right_path, left_path, up_path, down_path, left_down_diagonal, right_down_diagonal, left_up_diagonal, right_up_diagonal)

    if win_condition in paths:
        return True
    return False


def play(board, players):
    player_1, player_2 = players.keys()
    symbol_1, symbol_2 = players.values()

    current_player, other_player = player_1, player_2
    current_symbol, other_symbol = symbol_1, symbol_2

    def game_start():
        print("This is the numeration of the board:")
        print_board(create_dummy_board())
        print(f"{player_1} starts first")
    game_start()

    available_positions = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }

    while True:
        choice = get_player_choice(current_player, available_positions)
        r_idx, c_idx = apply_player_choice(board, choice, available_positions, current_symbol)
        success = check_win_condition(board, r_idx, c_idx, current_symbol)
        print_board(board)

        if success:
            print(f"{current_player} won!")
            break

        if not available_positions:
            print("Draw")
            break

        current_player, other_player = other_player, current_player
        current_symbol, other_symbol = other_symbol, current_symbol


play_a_game = 'y'

players = player_setup()


while play_a_game == 'y':
    board = create_board()
    play(board, players)

    play_a_game = input("Play another game: 'y'/'n'?\n")
