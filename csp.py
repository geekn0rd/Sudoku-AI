class Constraint:
    def __init__(self, variables, type):
        self.variables = variables
        self.type = type

    def is_satisfied(self, assignment):
        # Check if the constraint is satisfied by the current assignment of values to variables
        if self.type == "row":
            values = [assignment[var] for var in self.variables]
            return len(set(values)) == len(values) and all(value != 0 for value in values)
        elif self.type == "column":
            values = [assignment[var] for var in self.variables]
            return len(set(values)) == len(values) and all(value != 0 for value in values)
        elif self.type == "subgrid":
            values = [assignment[var] for var in self.variables]
            return len(set(values)) == len(values) and all(value != 0 for value in values)
        else:
            return True


class Variable:
    def __init__(self, row, col, domain):
        self.row = row
        self.col = col
        self.domain = domain
        self.value = None

    def assign(self, value):
        self.value = value

    def unassign(self):
        self.value = None

    def is_assigned(self):
        return self.value is not None
    
    def get_possible_values(self):
        if self.is_assigned():
            return [self.value]
        else:
            return self.domain