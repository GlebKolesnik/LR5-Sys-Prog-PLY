class NumNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value
    def generate_code(self):
        return str(self.value)

class BinOpNode:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self):
        if self.op == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.op == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.op == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.op == '/':
            return self.left.evaluate() / self.right.evaluate()
        elif self.op == '^':
            return self.left.evaluate() ** self.right.evaluate()
        else:
            raise Exception(f"Unknown operator: {self.op}")

    def generate_code(self):
        left_code = self.left.generate_code()
        right_code = self.right.generate_code()
        return f"({left_code} {self.op} {right_code})"
