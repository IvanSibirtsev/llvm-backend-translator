
from core.registers import Registers
from core.assembler.assembler import Assembler
from core.llvm.function import Function
from core.transalators.codeBlockTranslator import CodeBlocksTranslator


class FunctionTranslator:
    def __init__(self):
        self.registers = Registers()

    def translate(self, functions: list[Function]) -> Assembler:
        assembler = Assembler()
        for function in functions:
            variables = self._get_assembler_variables(function)
            variables_set = self._set_registers(function)
            assembler.extend(variables)
            blocks = function.code_blocks
            func_name = function.get_function_name()
            code_block_translator = CodeBlocksTranslator(self.registers, func_name, variables_set)
            assembler.extend(code_block_translator.translate(blocks))
        return assembler

    def _get_assembler_variables(self, function: Function) -> list[str]:
        args = function.get_in_args()
        assembler = []
        for index, arg in enumerate(args):
            assembler.append(f"{function.get_function_name()}_in_{index}:")
            assembler.append("0")
        return assembler

    def _set_registers(self, function: Function) -> list[str]:
        args = function.get_in_args()
        assembler = []
        self.registers.set_suffix(function.get_function_name())
        for index, arg in enumerate(args):
            register = self.registers.get_new_register_name()
            self.registers.set_variable_to_register(register, arg)
            assembler.append(f"mov {register}, {function.get_function_name()}_in_{index}")
        return assembler
