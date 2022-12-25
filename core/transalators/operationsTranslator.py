
from core.registers import Registers
from core.llvm.line import Line


class OperationsTranslator:

    map = {
        "add": "add",
        "sub": "sub",
        "mul": "mul",
        "sdiv": "div",
        "udiv": "div",
        "icmp": "icmp"
    }

    def __init__(self, registers: Registers):
        self.registers = registers

    def translate(self, calculation: Line) -> list[str]:
        assembler = []
        variables = calculation.get_variables()
        values = calculation.get_values()
        operation = calculation.get_operation()
        assembler_operation = self.map[operation]

        if len(variables) < 3 and len(values) >= 1:
            new_register, register_1, value = self._get_operands_with_constant(calculation)
            prefix = "rc"
        else:
            new_register, register_1, value = self._get_operands_with_variable(calculation)
            prefix = "rr"

        assembler.append(f"mov {new_register}, {register_1}")
        assembler.append(f"{assembler_operation}_{prefix} {new_register}, {value}")

        return assembler

    def _get_operands_with_constant(self, line: Line) -> [str, str, str]:
        variables = line.get_variables()
        constant = line.get_values()[0]
        assignment_variable = variables[0]
        new_register = self.registers.get_register_name_or_create_new(assignment_variable)
        register_1 = self.registers.get_register_name_by_variable(variables[1])
        return new_register, register_1, constant

    def _get_operands_with_variable(self, line: Line) -> [str, str, str]:
        variables = line.get_variables()
        assignment_variable = variables[0]
        new_register = self.registers.get_register_name_or_create_new(assignment_variable)
        self.registers.set_variable_to_register(new_register, assignment_variable)
        register_1 = self.registers.get_register_name_by_variable(variables[1])
        register_2 = self.registers.get_register_name_by_variable(variables[2])
        return new_register, register_1, register_2
