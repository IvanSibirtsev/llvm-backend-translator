
from core.registers import Registers
from core.llvm.line import Line


class AssignmentsTranslator:
    def __init__(self, registers: Registers):
        self.registers = registers

    def translate(self, assignment: Line):
        assembler = []
        variables = assignment.get_variables()
        variable = variables[0]
        register_1 = self.registers.get_register_name_or_create_new(variable)
        self.registers.set_variable_to_register(register_1, variable)

        if assignment.is_variable_assignment():
            var_2 = self.registers.get_register_name_by_variable(variables[1])
        else:
            var_2 = assignment.get_values()[0]

        assembler_line = f"mov {register_1}, "

        if assignment.is_variable_assignment():
            assembler_line += f"{var_2}"
        if assignment.is_constant_assignment():
            assembler_line += f"{var_2}"

        assembler.append(assembler_line)
        return assembler
