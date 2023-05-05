class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
    
    def ac3(self, queue=None):
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
    
    def revise(self, xi, xj):
        revised = False
        for x in set(self.domains[xi]):
            if not any([self.constraints(xi, x, xj, y) for y in self.domains[xj]]):
                self.domains[xi].remove(x)
                revised = True
        return revised
    
    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None
    
    def select_unassigned_variable(self, assignment):
        unassigned = [v for v in self.variables if v not in assignment]
        return self.most_constrained_variable(unassigned)
    
    def order_domain_values(self, var, assignment):
        return self.domains[var]
    
    def is_consistent(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and not self.constraints(var, value, neighbor, assignment[neighbor]):
                return False
        return True
    
    def most_constrained_variable(self, variables):
        return min(variables, key=lambda var: len(self.domains[var]))