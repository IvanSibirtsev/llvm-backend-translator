from core.llvm.line import Line


class CodeBlock:
    def __init__(self, lines: list[Line], name: str):
        self.name = name
        self.lines = lines
