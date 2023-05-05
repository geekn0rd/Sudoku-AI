from typing import List

class Variable:
    def __init__(self, row: int, col: int, domain: List[int]):
        self.row = row
        self.col = col
        self.domain = domain
        self.value =  None if len(domain) > 1 else domain[0]

    def __str__(self):
        return f'({self.row}, {self.col}): {self.value}'


class Constraint:
    def __init__(self, variables: List[Variable]):
        self.variables = variables

    def is_satisfied(self, assignment: List[Variable]) -> bool:
        pass

    def __str__(self):
        return f'{[var for var in self.variables]}'


class SudokuConstraint(Constraint):
    def __init__(self, variables: List[Variable]):
        super().__init__(variables)

    def is_satisfied(self, assignment: List[Variable]) -> bool:
        values = [var.value for var in assignment if var in self.variables]
        #print(values)
        return len(values) == len(set(values))


class CSP:
    def __init__(self, variables: List[Variable], constraints: List[Constraint]):
        self.variables = variables
        self.constraints = constraints

    def get_related_variables(self, var: Variable) -> List[Variable]:
        related_vars = []
        for constraint in self.constraints:
            if var in constraint.variables:
                for related_var in constraint.variables:
                    if related_var != var and related_var not in related_vars:
                        related_vars.append(related_var)
        return related_vars

    def is_consistent(self, var: Variable, value: int, assignment: List[Variable]) -> bool:
        var.value = value
        assignment.append(var)
        for constraint in self.constraints:
            if not constraint.is_satisfied(assignment):
                var.value = None
                assignment.pop()
                return False
        var.value = None
        assignment.pop()
        return True

    def assign(self, var: Variable, value: int):
        var.value = value

    def unassign(self, var: Variable):
        var.value = None

def mrv(csp: CSP, assignment: List[Variable]) -> Variable:
    unassigned_vars = [var for var in csp.variables if var.value is None]
    sorted_vars = sorted(unassigned_vars, key=lambda var: len(var.domain))
    return sorted_vars[0]

def ac3(csp: CSP, queue: List[tuple]) -> bool:
    while queue:
        (Xi, Xj) = queue.pop(0)
        if revise(csp, Xi, Xj):
            if len(Xi.domain) == 0:
                return False
            for Xk in csp.get_related_variables(Xi):
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True

def revise(csp: CSP, Xi: Variable, Xj: Variable) -> bool:
    revised = False
    for value in Xi.domain:
        if not csp.is_consistent(Xi, value, [csp.assign(Xj, value)]):
            Xi.domain.remove(value)
            revised = True
    return revised

def order_domain_values(var: Variable, assignment: List[Variable], csp: CSP) -> List[int]:
    return var.domain

def backtrack(csp: CSP, assignment: List[Variable]=[]) -> List[Variable]:
    if all(var.value is not None for var in csp.variables):
        return assignment
    var = mrv(csp, assignment)
    for value in order_domain_values(var, assignment, csp):
        if csp.is_consistent(var, value, assignment):
            csp.assign(var, value)
            assignment.append(var)
            # queue = [(related_var, var) for related_var in csp.get_related_variables(var)]
            # if ac3(csp, queue):
            #     result = backtrack(csp, assignment)
            #     if result is not None:
            #         return result
            result = backtrack(csp, assignment)
            if result is not None:
                return result
            csp.unassign(var)
            assignment.pop()
    return None