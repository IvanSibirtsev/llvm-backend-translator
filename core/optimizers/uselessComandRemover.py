from core.assembler.command import Command, NotCommand, AssemblerCode


class UselessCommandRemover:
    def optimize(self, commands: AssemblerCode) -> AssemblerCode:
        return [command for command in commands if not self._not_need(command)]

    def _not_need(self, command: Command | NotCommand) -> bool:
        return isinstance(command, Command) and command.is_mov() and command.left == command.right
