def print_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'X'):
        return 1
    if check_winner(board, 'O'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter column (0,1,2): "))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Cell already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        # Human
        human_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # AI
        i, j = best_move(board)
        board[i][j] = 'X'
        print("AI played:")
        print_board(board)
        if check_winner(board, 'X'):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

play_game()