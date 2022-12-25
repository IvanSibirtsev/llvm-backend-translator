from core.assembler.command import NotCommand, AssemblerCode


def get_lines_with_usage(commands: AssemblerCode) -> dict[str, list[int]]:
    result = {}
    for index, command in enumerate(commands):

        if isinstance(command, NotCommand):
            continue

        if command.left in result.keys():
            result[command.left].append(index)

        if command.right in result.keys():
            result[command.right].append(index)

        if command.left not in result.keys():
            result[command.left] = [index]
        if command.right not in result.keys() and not command.right_is_register():
            result[command.right] = [index]

    return result
