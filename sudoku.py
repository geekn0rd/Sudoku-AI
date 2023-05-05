from csp import CSP

def sudoku_csp(grid):
    variables = []
    domains = {}
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                variables.append((i, j))
                domains[(i, j)] = set(range(1, 10))
            else:
                domains[(i, j)] = set([grid[i][j]])
    neighbors = {}
    for i in range(9):
        for j in range(9):
            row = [(i, y) for y in range(9) if y != j]
            col = [(x, j) for x in range(9) if x != i]
            box = [(x, y) for x in range((i//3)*3, (i//3)*3+3) 
                          for y in range((j//3)*3, (j//3)*3+3) if x != i or y != j]
            neighbors[(i, j)] = set(row + col + box)
    constraints = lambda xi, x, xj, y: x != y
    return CSP(variables, domains, neighbors, constraints)

def solve_sudoku(grid):
    csp = sudoku_csp(grid)
    csp.ac3()
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found")
    else:
        for i in range(9):
            for j in range(9):
                if (i, j) in solution:
                    grid[i][j] = solution[(i, j)]
        return grid