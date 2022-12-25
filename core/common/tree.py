from core.assembler.command import Command, AssemblerCode


class Tree:
    def __init__(self, initial_command: Command, position: int):
        self.position = position
        self.command = initial_command
        self.children: list['Tree'] = []

    def add_child(self, tree: 'Tree'):
        self.children.append(tree)

    def make_line_optimization(self, register, prev_reg_to_opt=""):
        cmd = self.command
        reg_to_optimize = self._define_reg_to_optimize(register, prev_reg_to_opt)
        if len(self.children) == 1:
            self._linearize(register, reg_to_optimize)
            if self.command.is_calc():
                register = reg_to_optimize
            self.children[0].make_line_optimization(register, reg_to_optimize)
        elif len(self.children) > 1:
            for child in self.children:
                child.make_line_optimization(reg_to_optimize, reg_to_optimize)
        else:
            self._linearize(register, reg_to_optimize)

    def _linearize(self, register: str, old_register: str):
        if self.command.is_mov():
            self.command.left = register
            if self.command.right_is_register():
                self.command.right = register
        elif not self.command.contains(register):
            if self.command.right_is_register() and self.command.right == old_register:
                self.command.right = register
            elif self.command.left == old_register:
                self.command.left = register

    def get_commands(self) -> dict[int, Command]:
        result = {self.position: self.command}
        for child in self.children:
            result.update(child.get_commands())
        return result

    def _flat(self) -> list['Tree']:
        result = self.children
        result.extend(self._flat())
        return result

    def _define_reg_to_optimize(self, reg: str, prev_reg_to_opt: str) -> str:
        left = self.command.left
        right = self.command.right
        if not self.command.right_is_register():
            return left
        if self.command.is_calc() and prev_reg_to_opt:
            return prev_reg_to_opt
        return right if left == reg else left


def create_tree(command: Command, usages: dict[str, list[int]], all_commands: AssemblerCode,
                current_position: int, visited: set[int]) -> Tree:
    register_usages = usages[command.left]
    tree = Tree(command, current_position)
    for usage in register_usages:
        if usage in visited:
            continue
        visited.add(usage)
        if usage <= current_position:
            continue
        command = all_commands[usage]
        child_tree = create_tree(command, usages, all_commands, usage, visited)
        tree.add_child(child_tree)

    return tree
