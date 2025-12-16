# =========================
# HELPER
# =========================

EMPTY = "." 
PLAYER_X = "X"
PLAYER_O = "O"

# In bàn cờ
def print_board(board):
    """In bàn cờ"""
    size = len(board) # kích thước bàn cờ
    print("\n  " + " ".join(str(i) for i in range(size))) # in tiêu đề cột
    for i in range(size): # in mỗi hàng với tiêu đề hàng
        print(i, " ".join(board[i]))
    print()


def get_available_moves(board): # trả về các ô trống
    """Lấy các ô trống"""
    return [(i, j) for i in range(len(board)) # duyệt qua các hàng
                    for j in range(len(board)) # duyệt qua các cột
                    if board[i][j] == EMPTY] # nếu ô trống thì thêm vào danh sách

# kiểm tra các trường hợp thắng cho người chơi (theo hàng, cột, chéo) - AI 
def check_winner(board, player, win_len=3): # kiểm tra thắng cho người chơi
    """Kiểm tra thắng"""
    n = len(board)# kích thước bàn cờ

    # Hàng & cột
    for i in range(n): # duyệt qua các hàng và cột
        for j in range(n - win_len + 1):# duyệt qua các vị trí có thể thắng
            # Kiểm tra hàng
            if all(board[i][j+k] == player for k in range(win_len)):# nếu tất cả các ô trong hàng đều là của người chơi
                return True # trả về thắng
            if all(board[j+k][i] == player for k in range(win_len)): # kiểm tra cột
                return True# trả về thắng

    # Chéo chính
    for i in range(n - win_len + 1):
        for j in range(n - win_len + 1):
            if all(board[i+k][j+k] == player for k in range(win_len)):
                return True

    # Chéo phụ
    for i in range(n - win_len + 1):
        for j in range(win_len - 1, n):
            if all(board[i+k][j-k] == player for k in range(win_len)):
                return True

    return False

# kiểm tra hòa
def is_draw(board):
    """Kiểm tra hòa"""
    return all(cell != EMPTY for row in board for cell in row)

# =========================
# CORE – MINIMAX + ALPHA-BETA
# =========================
# Đánh giá trạng thái bàn cờ
def evaluate(board, ai, human):
    if check_winner(board, ai): # nếu AI thắng
        return 10
    if check_winner(board, human): # nếu người chơi thắng
        return -10
    return 0


def minimax(board, depth, alpha, beta, is_maximizing, ai, human): # minimax với cắt tỉa alpha-beta
    score = evaluate(board, ai, human) # gán giá trị đánh giá bàn cờ

    if score != 0 or is_draw(board) or depth == 0: # nếu có người thắng hoặc hòa hoặc đạt độ sâu tối đa
        return score # trả về giá trị đánh giá

    if is_maximizing: # nếu là lượt của AI
        best = -float("inf") # khởi tạo best là âm vô cực
        for (i, j) in get_available_moves(board): # duyệt qua các ô trống
            board[i][j] = ai # đặt quân AI vào ô trống
            val = minimax(board, depth - 1, alpha, beta, False, ai, human) # gọi đệ quy minimax cho lượt người chơi
            board[i][j] = EMPTY# bỏ quân AI khỏi ô trống
            best = max(best, val) # cập nhật best nếu val lớn hơn
            alpha = max(alpha, val) # cập nhật alpha 
            if beta <= alpha: # cắt tỉa
                break
        return best# trả về best giá trị tốt nhất cho AI
    else:
        best = float("inf") # khởi tạo best là dương vô cực
        for (i, j) in get_available_moves(board): # duyệt qua các ô trống
            board[i][j] = human # đặt quân người chơi vào ô trống
            val = minimax(board, depth - 1, alpha, beta, True, ai, human) # gọi đệ quy minimax cho lượt AI
            board[i][j] = EMPTY
            best = min(best, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return best


def best_move(board, depth, ai, human):
    best_score = -float("inf")
    move = None

    for (i, j) in get_available_moves(board):
        board[i][j] = ai
        score = minimax(board, depth, -float("inf"), float("inf"),
                        False, ai, human)
        board[i][j] = EMPTY

        if score > best_score:
            best_score = score
            move = (i, j)

    return move


