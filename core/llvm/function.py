import re

from core.llvm.codeBlock import CodeBlock
from core.llvm.line import Line


class Function:
    def __init__(self, code_blocks: list[CodeBlock], declaration: Line):
        self._declaration = declaration
        self.code_blocks = code_blocks

    def get_in_args(self) -> list[str]:
        return self._declaration.get_variables()

    def get_function_name(self) -> str:
        name = [name for name in self._declaration.get_values() if name.startswith('@')][0]
        name = name.replace("?", "")
        if '"' in name:
            return "@" + re.findall(r"\"(.*?)\"", name)[0]
        return name
