def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
 
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
 
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
 
    return True
 
def solve_n_queens(board, row, n):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
        print()
        return
 
    for j in range(n):
        if is_safe(board, row, j, n):
            board[row][j] = 1
            solve_n_queens(board, row + 1, n)
            board[row][j] = 0
 
n = int(input("Enter the value of n: "))
board = [[0] * n for _ in range(n)]
 
solve_n_queens(board, 0, n)
