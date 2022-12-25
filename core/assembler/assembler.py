from core.assembler.command import Command, Label, Number
from core.common.formatter import Formatter


class Assembler:
    def __init__(self):
        self._lines = []
        self.lines_to_optimize = []

    def append(self, line: str):
        self._lines.append(line)
        if ":" not in line:
            line = line.replace(",", "")
            t = line.split()
            if len(t) < 3:
                self.lines_to_optimize.append(Number(t[0]))
            else:
                self.lines_to_optimize.append(Command(t[1], t[2], t[0]))
        else:
            self.lines_to_optimize.append(Label(line))

    def extend(self, lines: list[str]):
        for line in lines:
            self.append(line)

    def __str__(self):
        formatted = Formatter.format(self._lines)
        return "\n".join(formatted)
