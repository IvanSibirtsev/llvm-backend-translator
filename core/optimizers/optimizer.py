from core.assembler.command import Command, AssemblerCode
from core.common.tree import create_tree
from core.common.util import get_lines_with_usage
from core.optimizers.sameLinesRemover import SameLinesRemover
from core.optimizers.uselessComandRemover import UselessCommandRemover


class Optimizer:
    def __init__(self):
        pass

    def optimize(self, commands_by_position: AssemblerCode):
        opt = SameLinesRemover()
        optimized = opt.optimize(commands_by_position)
        index = 0
        while index < len(optimized):
            command = optimized[index]
            if isinstance(command, Command):
                usages = get_lines_with_usage(optimized)
                tree = create_tree(command, usages, optimized, index, set())
                tree.make_line_optimization(command.left)
                commands_by_position = tree.get_commands()
                self._replace(commands_by_position, optimized)
            index += 1

        ucr = UselessCommandRemover()
        #optimized = ucr.optimize(optimized)

        return optimized

    def _replace(self, lines_to_replace: dict[int, Command], commands: AssemblerCode):
        for key in lines_to_replace:
            commands[key] = lines_to_replace[key]