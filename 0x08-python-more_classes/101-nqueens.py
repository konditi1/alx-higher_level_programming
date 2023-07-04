#!/usr/bin/python3
"""
Check if the current position is safe for a queen
"""


import sys

def is_safe(board, row, col):
    # Check if the current position is safe for a queen
    
    # Check the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True


def solve_nqueens(N):
    def backtrack(board, col, solutions):
        if col >= N:
            # All queens have been placed, add the solution
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return
        
        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, col + 1, solutions)
                board[row][col] = 0
    
    # Check if N is a valid integer
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0] * N for _ in range(N)]
    
    solutions = []
    backtrack(board, 0, solutions)
    
    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Solve the N Queens problem
    solve_nqueens(sys.argv[1])

