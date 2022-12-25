
from core.registers import Registers
from core.llvm.codeBlock import CodeBlock
from core.transalators.lineTranslator import LineTranslator


class CodeBlocksTranslator:
    def __init__(self, registers: Registers, func_name: str, in_args_init: list[str]):
        self.in_args_init = in_args_init
        self.func_name = func_name
        self.registers = registers

    def translate(self, blocks: list[CodeBlock]) -> list[str]:
        assembler = [self.func_name + ":"]
        assembler.extend(self.in_args_init)
        for block in blocks:
            translator = LineTranslator(self.registers)
            if block.name:
                assembler.append("label_" + block.name + ":")
            block_assembler = translator.translate(block.lines)
            assembler.extend(block_assembler)

        return assembler
