from csp import *

def solve_sudoku_csp(board: list[list[int]]) -> list[list[int]]:
    variables = []
    constraints = []
    assignment = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domain = list(range(1, 10))
            else:
                domain = [board[i][j]]
            variable = Variable(i, j, domain)
            if board[i][j] != 0:
                assignment.append(variable)
            variables.append(variable)

    for i in range(9):
        row_vars = [var for var in variables if var.row == i]
        row_constraint = SudokuConstraint(row_vars)
        #print(*row_vars)
        constraints.append(row_constraint)

    for j in range(9):
        col_vars = [var for var in variables if var.col == j]
        col_constraint = SudokuConstraint(col_vars)
        #print(*col_vars)
        constraints.append(col_constraint)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block_vars = [var for var in variables if var.row in range(i, i+3) and var.col in range(j, j+3)]
            block_constraint = SudokuConstraint(block_vars)
            #print(*block_vars)
            constraints.append(block_constraint)
    
    csp = CSP(variables, constraints)
    result = backtrack(csp, assignment)
    if result is not None:
        for var in result:
            board[var.row][var.col] = var.value
    # for const in constraints:
    #     print(*const.variables)

    return board