
from core.registers import Registers
from core.llvm.line import Line


class DeclarationTranslator:
    def __init__(self, registers: Registers):
        self.registers = registers

    def translate(self, declaration: Line) -> list[str]:
        assembler = []
        variable = declaration.get_left_operand().value
        value = self._get_default(declaration)
        register = self.registers.get_new_register_name()
        self.registers.set_variable_to_register(register, variable)
        assembler.append(f"mov {register}, {value}")
        return assembler

    def _get_default(self, declaration):
        if declaration.get_types()[0].startswith("i"):
            return "0"
        return "!default!"
