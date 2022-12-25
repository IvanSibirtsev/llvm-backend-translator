class AssemblerLine:
    def __init__(self, left: str, right: str, operation: str):
        self.left = left
        self.right = right
        self.operation = operation

    def __str__(self):
        return f"{self.operation}, {self.left}, {self.right}"
