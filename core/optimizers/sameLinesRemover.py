from core.assembler.command import Command, AssemblerCode
from core.common.util import get_lines_with_usage


class SameLinesRemover:
    def __init__(self):
        pass

    def optimize(self, commands: AssemblerCode) -> AssemblerCode:
        optimized = []
        usages = get_lines_with_usage(commands)
        i = 0
        need_to_remove = []
        while i < len(commands):

            command = commands[i]
            if not isinstance(command, Command):
                i += 1
                optimized.append(command)
                continue

            suffix = commands[i + 1:]
            if command in suffix:
                index = suffix.index(command)
                if index <= max(usages[command.left]):
                    need_to_remove.append(index + i + 1)

            if i not in need_to_remove:
                optimized.append(command)

            i += 1
        return optimized
