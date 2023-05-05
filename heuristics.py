from csp import CSP, Variable
from typing import List

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
        if not any(csp.is_consistent(Xi, value, [Xj.assign(value)])):
            Xi.domain.remove(value)
            revised = True
    return revised

def order_domain_values(var: Variable, assignment: List[Variable], csp: CSP) -> List[int]:
    return var.domain