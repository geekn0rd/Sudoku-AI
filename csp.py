class CSP:
    def __init__(self, variables: list, domains: dict, neighbors: dict, constraints: function):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
    
    def ac3(self, queue: list = None) -> bool:
        if queue is None:
            queue = [(i, j) for i in self.variables for j in self.neighbors[i]]
        while queue:
            (xi, xj) = queue.pop(0)
            if self.revise(xi, xj):
                if not self.domains[xi]:
                    return False
                for xk in self.neighbors[xi]:
                    if xk != xj:
                        queue.append((xk, xi))
        return True
    
    def revise(self, xi: tuple, xj: tuple) -> bool:
        revised = False
        for x in set(self.domains[xi]):
            if not any([self.constraints(xi, x, xj, y) for y in self.domains[xj]]):
                self.domains[xi].remove(x)
                revised = True
        return revised
    
    def backtracking_search(self, assignment: dict = {}) -> dict:
        if len(assignment) == len(self.variables):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None
    
    def select_unassigned_variable(self, assignment: dict) -> list:
        unassigned = [v for v in self.variables if v not in assignment]
        return self.min_remaining_values(unassigned)
    
    def order_domain_values(self, var: tuple) -> list:
        return self.domains[var]
    
    def is_consistent(self, var: tuple, value: int, assignment: dict) -> bool:
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and not self.constraints(var, value, neighbor, assignment[neighbor]):
                return False
        return True
    
    def min_remaining_values(self, variables: list) -> tuple:
        return min(variables, key=lambda var: len(self.domains[var]))