from csp import Constraint

class SudokuBoard:
    def __init__(self, board):
        self.board = board
        self.variables = [(i, j) for i in range(9) for j in range(9)]
        self.domains = {(i, j): set(range(1, 10)) if board[i][j] == 0 else set([board[i][j]]) for i in range(9) for j in range(9)}
        self.constraints = self.create_constraints()

    def create_constraints(self):
        # Create a list of constraints based on the Sudoku rules
        constraints = []
        for i in range(9):
            row_vars = [(i, j) for j in range(9)]
            col_vars = [(j, i) for j in range(9)]
            subgrid_vars = [(i//3*3+j//3, i%3*3+j%3) for j in range(9)]
            constraints += [Constraint(row_vars, "row"), Constraint(col_vars, "column"), Constraint(subgrid_vars, "subgrid")]
        return constraints
