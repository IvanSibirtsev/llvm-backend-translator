from core.assembler.command import Command, Label, Number, AssemblerCode


class Assembler:
    def __init__(self):
        self._lines = []
        self._lines_to_optimize = []

    def append(self, line: str):
        self._lines.append(line)
        if ":" not in line:
            line = line.replace(",", "")
            t = line.split()
            if len(t) < 3:
                self._lines_to_optimize.append(Number(t[0]))
            else:
                self._lines_to_optimize.append(Command(t[1], t[2], t[0]))
        else:
            self._lines_to_optimize.append(Label(line))

    def extend(self, lines: list[str]):
        for line in lines:
            self.append(line)

    @property
    def lines(self) -> list[str]:
        return self._lines

    @property
    def lines_to_optimize(self) -> list[AssemblerCode]:
        return self._lines_to_optimize
