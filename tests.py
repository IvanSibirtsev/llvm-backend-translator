import unittest

from core.common.formatter import Command
from core.optimizers.optimizer import Optimizer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        strings = [
            "mov r1, 0",
            "mov r2, 0",
            "mov r3, 0",
            "mov r4, 0",
            "mov r1, 0",
            'mov r2, 5',
            'mov r5, r2',
            'mov r6, r5',
            'icmp_rc r6, 4'
        ]

        commands = create_commands(strings)
        opt = Optimizer()
        optimized = opt.optimize(commands)
        for c in optimized:
            print(c)


def create_commands(strings: list[str]) -> list[Command]:
    commands = []
    for string in strings:
        string = string.replace(",", "")
        splt = string.split()
        commands.append(Command(splt[1], splt[2], splt[0]))
    return commands


if __name__ == '__main__':
    unittest.main()
