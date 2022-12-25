class Command:
    def __init__(self, left: str, right: str, operation: str):
        self.operation = operation
        self.right = right
        self.left = left

    def right_is_register(self) -> bool:
        return self.right.startswith("r")

    def left_is_register(self) -> bool:
        return self.left.startswith("r")

    def is_mov(self) -> bool:
        return self.operation == 'mov'

    def is_calc(self) -> bool:
        return self.operation != 'mov'

    def contains(self, register: str) -> bool:
        return register in [self.right, self.left]

    def __eq__(self, other):
        return isinstance(other, Command) and self.right == other.right and \
               self.left == other.left and self.operation == other.operation

    def __str__(self) -> str:
        return f"{self.operation} {self.left}, {self.right}"


class Label:
    def __init__(self, label: str):
        self.label = label

    def __str__(self):
        return self.label


class Number:
    def __init__(self, number: str):
        self.number = number

    def __str__(self):
        return f"{self.number}"


NotCommand = Label | Number

AssemblerCode = list[Command | NotCommand]
