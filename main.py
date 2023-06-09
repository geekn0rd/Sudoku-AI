from sudoku import solve_sudoku
import time

# grid = [
#     [0, 2, 6, 0, 0, 0, 8, 1, 0],
#     [3, 0, 0, 7, 0, 8, 0, 0, 6],
#     [4, 0, 0, 0, 5, 0, 0, 0, 7],
#     [0, 5, 0, 1, 0, 7, 0, 9, 0],
#     [0, 0, 3, 9, 0, 5, 1, 0, 0],
#     [0, 4, 0, 3, 0, 2, 0, 5, 0],
#     [1, 0, 0, 0, 3, 0, 0, 0, 2],
#     [5, 0, 0, 2, 0, 4, 0, 0, 9],
#     [0, 3, 8, 0, 0, 0, 4, 6, 0]
# ]

# 
# grid = [
#     [8, 15, 11, 1, 6, 2, 10, 14, 12, 7, 13, 3, 16, 9, 4, 5],
#     [10, 6, 3, 16, 12, 5, 8, 4, 14, 15, 1, 9, 2, 11, 7, 13],
#     [14, 5, 9, 7, 11, 3, 15, 13, 8, 2, 16, 4, 12, 10, 1, 6],
#     [4, 13, 2, 12, 1, 9, 7, 16, 6, 10, 5, 11, 3, 15, 8, 14],
#     [9, 2, 6, 15, 14, 1, 11, 7, 3, 5, 10, 16, 4 ,8 ,13 ,12],
#     [3, 16, 12, 8, 2, 4, 6, 9, 11, 14, 7, 13, 10, 1, 5, 15],
#     [11, 10, 5, 13, 8, 12, 3, 15, 1, 9, 4, 2, 7, 6, 14, 16],
#     [1, 4, 7, 14, 13, 10, 16, 5, 15, 6, 8, 12, 9, 2, 3, 11],
#     [13, 7, 16, 5, 9, 6, 1, 12, 2, 8, 3, 10, 11, 14, 15, 4],
#     [2, 12, 8, 11, 7, 16, 14, 3, 5, 4, 6, 15, 1, 13, 9, 10],
#     [6, 3, 14, 4, 10, 15, 13, 8, 7, 11, 9, 1, 5, 12, 16, 2],
#     [15, 1, 10, 9, 4, 11, 5, 2, 13, 16, 12, 14, 8, 3, 6, 7],
#     [12, 8, 4, 3, 16, 7, 2, 10, 9, 13, 14, 6, 15, 5 ,11 ,1],
#     [5, 11, 13, 2, 3, 8, 4, 6, 10, 1, 15, 7, 14, 16, 12, 9],
#     [7, 9, 1, 6, 15, 14, 12, 11, 16, 3, 2, 5, 13, 4, 10, 8],
#     [16, 14, 15, 10, 5, 13, 9, 1, 4, 12, 11, 8, 6, 7, 2, 3],
# ]

# n = len(grid[0])
# solution = solve_sudoku(grid, n)

# # Print the solution
# if solution is not None:
#     print("Solution:")
#     for i in range(n):
#         for j in range(n):
#             print(solution[i][j], end=' ')
#         print()

if __name__ == "__main__":
    # Get the inputs
    n = int(input())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    c = int(input())
    for _ in range(c):
        i, j, value = map(int, input().split())
        i -= 1
        j -= 1
        grid[i][j] = value
    # Mesaure time
    start_time = time.time()
    # Solve the Sudoku puzzle using CSP and AC3 algorithm
    solution = solve_sudoku(grid, n)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Elapsed time: {:.3f} seconds".format(elapsed_time))

    # Print the solution
    if solution is not None:
        print("Solution:")
        for i in range(n):
            for j in range(n):
                print(solution[i][j], end=' ')
            print()