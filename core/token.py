from core.tokenType import TokenType


class Token:
    def __init__(self, value, token_type: TokenType):
        self.token_type = token_type
        self.value = value
        self._simplify()

    def _simplify(self):
        if self.token_type == TokenType.Label:
            self.value = self.value.replace(":", "")

        if self.token_type == TokenType.New_Line:
            self.value = ""

    def is_variable(self) -> bool:
        return self.token_type == TokenType.Variable

    def is_new_line(self) -> bool:
        return self.token_type == TokenType.New_Line

    def is_value(self) -> bool:
        return self.token_type == TokenType.Value

    def is_type(self) -> bool:
        return self.token_type == TokenType.Type

    def is_operation(self) -> bool:
        return self.token_type == TokenType.Operation

    def is_function_declaration(self) -> bool:
        return self.token_type == TokenType.Function_Declaration

    def __str__(self) -> str:
        return f"{self.value}:{self.token_type}"
