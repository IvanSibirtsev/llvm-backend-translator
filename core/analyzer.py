
from core.token import Token
from core.tokenType import TokenType as TT, Details
from core.tokenType import Semantic
from core.llvm.codeBlock import CodeBlock
from core.llvm.function import Function
from core.llvm.line import Line


class Analyzer:
    def analyze_to_lines(self, tokens: list[Token]) -> list[Line]:
        lines = self._split_to_lines(tokens)
        result = []
        for index, line in enumerate(lines):
            sematic = self._define_semantic(line)
            details = self._define_details(line)
            result.append(Line(sematic, line, index, details))

        return result

    def analyze_to_blocks(self, lines: list[Line]) -> list[CodeBlock]:
        blocks = []
        inner_block_lines = []
        block_name = ""
        for line in lines:

            if line.is_label_declaration():
                block_name = line.tokens[0].value
                continue

            if line.has_label_call():
                inner_block_lines.append(line)
                block = CodeBlock(inner_block_lines, block_name)
                blocks.append(block)
                inner_block_lines = []
                continue

            inner_block_lines.append(line)

        if inner_block_lines:
            block = CodeBlock(inner_block_lines, block_name)
            blocks.append(block)

        return blocks

    def analyze_to_functions(self, lines: list[Line]) -> list[Function]:
        functions = []
        inner_code_blocks = []
        declaration_line = ""
        for line in lines:
            values = line.get_values()
            if line.is_func_declaration():
                if values[0] == "}":
                    code_blocks = self.analyze_to_blocks(inner_code_blocks)
                    functions.append(Function(code_blocks, declaration_line))
                    inner_code_blocks = []
                    continue
                else:
                    declaration_line = line
                    continue

            inner_code_blocks.append(line)
        return functions

    def _split_to_lines(self, tokens: list[Token]) -> list[list[Token]]:
        i = 0
        result = []
        while i < len(tokens):
            token = tokens[i]
            if token.is_new_line():
                i += 1
                inner_result = []
                while i < len(tokens) and not tokens[i].is_new_line():
                    token = tokens[i]
                    inner_result.append(token)
                    i += 1
                if inner_result:
                    result.append(inner_result)
        return result

    def _define_semantic(self, line: list[Token]) -> Semantic:
        if self._is_declaration(line):
            return Semantic.DECLARATION

        if self._is_assignment(line):
            return Semantic.ASSIGNMENT

        if self._is_function_declaration(line):
            return Semantic.FUNCTION_DECLARATION

        if self._is_transfer(line):
            return Semantic.TRANSFER

        return Semantic.CALCULATION

    def _is_declaration(self, line: list[Token]) -> bool:
        types = [token.token_type for token in line]
        return [TT.Variable, TT.Assignment, TT.Memory_Access, TT.Type] == types

    def _is_assignment(self, line: list[Token]) -> bool:
        types = [token.token_type for token in line]
        return [TT.Memory_Access, TT.Type, TT.Value, TT.Type, TT.Variable] == types or \
               [TT.Variable, TT.Assignment, TT.Memory_Access, TT.Type, TT.Type, TT.Variable] == types or \
               [TT.Memory_Access, TT.Type, TT.Variable, TT.Type, TT.Variable] == types

    def _is_function_declaration(self, line: list[Token]) -> bool:
        types = [token.token_type for token in line]
        values = [token.value for token in line]
        return TT.Function_Declaration in types or len(values) >= 1 and values[0] == "}"

    def _is_transfer(self, line: list[Token]) -> bool:
        types = [token.token_type for token in line]
        return TT.Transfer in types

    def _is_calculation(self, line: list[Token]) -> bool:
        return True

    def _define_details(self, line: list[Token]) -> Details:
        variables = [token.value for token in line if token.is_variable()]
        constants = [token.value for token in line if token.is_value()]
        if len(variables) == 2:
            return Details.Variable_Assignment
        if len(constants) == 1 and len(variables) == 1:
            return Details.Constant_Assignment

        return Details.No
