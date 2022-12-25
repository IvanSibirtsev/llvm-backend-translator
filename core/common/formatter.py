from core.assembler.command import Command, Number, AssemblerCode


class Formatter:
    @staticmethod
    def format(assembler: list[str]) -> list[str]:
        lines = []
        for command in assembler:
            if ":" in command:
                lines.append("")
                lines.append(command)
                continue
            lines.append("\t" + command)

        return lines

    @staticmethod
    def format_commands(assembler: AssemblerCode) -> list[str]:
        lines = []
        for command in assembler:
            if isinstance(command, Command):
                lines.append(f"\t{str(command)}")
            elif isinstance(command, Number):
                lines.append(f"\t{str(command)}")
            else:
                lines.append("")
                lines.append(str(command))
        return lines
