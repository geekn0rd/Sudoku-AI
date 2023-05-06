from csp import CSP

def sudoku_csp(grid, n=9):
    variables = []
    domains = {}
    root_n = int(n**0.5)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                variables.append((i, j))
                domains[(i, j)] = set(range(1, n + 1))
            else:
                domains[(i, j)] = set([grid[i][j]])
    neighbors = {}
    for i in range(n):
        for j in range(n):
            row = [(i, y) for y in range(n) if y != j]
            col = [(x, j) for x in range(n) if x != i]
            box = [(x, y) for x in range((i//root_n)*root_n, (i//root_n)*root_n+root_n) 
                          for y in range((j//root_n)*root_n, (j//root_n)*root_n+root_n) if x != i or y != j]
            neighbors[(i, j)] = set(row + col + box)
    constraints = lambda xi, x, xj, y: x != y
    return CSP(variables, domains, neighbors, constraints)

def solve_sudoku(grid, n=9):
    csp = sudoku_csp(grid, n)
    csp.ac3()
    solution = csp.backtracking_search()
    if solution is None:
        print("Unsolvable CSP!")
    else:
        for i in range(n):
            for j in range(n):
                if (i, j) in solution:
                    grid[i][j] = solution[(i, j)]
        return grid