
from core.registers import Registers
from core.llvm.line import Line
from core.transalators.assignmentTranslator import AssignmentsTranslator
from core.transalators.declarationTranslator import DeclarationTranslator
from core.transalators.operationsTranslator import OperationsTranslator


class LineTranslator:
    registers_count = 1

    def __init__(self, registers: Registers):
        self.registers = registers

    def translate(self, lines: list[Line]) -> list[str]:
        assembler = []
        declaration_translator = DeclarationTranslator(self.registers)
        assignments_translator = AssignmentsTranslator(self.registers)
        operations_translator = OperationsTranslator(self.registers)

        for line in lines:
            if line.is_declaration():
                assembler.extend(declaration_translator.translate(line))

            if line.is_assignment():
                assembler.extend(assignments_translator.translate(line))

            if line.is_calculation():
                assembler.extend(operations_translator.translate(line))

        return assembler
