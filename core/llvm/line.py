from core.token import Token
from core.tokenType import Semantic, Details, TokenType


class Line:
    def __init__(self, sematic: Semantic, tokens: list[Token], position: int, details: Details = Details.No):
        self.details = details
        self.position = position
        self.tokens = tokens
        self.sematic = sematic

    def is_declaration(self) -> bool:
        return self.sematic == Semantic.DECLARATION

    def is_assignment(self) -> bool:
        return self.sematic == Semantic.ASSIGNMENT

    def is_calculation(self) -> bool:
        return self.sematic == Semantic.CALCULATION

    def is_variable_assignment(self) -> bool:
        return self.details == Details.Variable_Assignment

    def is_constant_assignment(self) -> bool:
        return self.details == Details.Constant_Assignment

    def is_label_declaration(self) -> bool:
        token_types = [token.token_type for token in self.tokens]
        return TokenType.Label in token_types

    def is_func_declaration(self) -> bool:
        return self.sematic == Semantic.FUNCTION_DECLARATION

    def has_label_call(self) -> bool:
        token_types = [token.token_type for token in self.tokens]
        return TokenType.Transfer in token_types

    def get_token_types(self) -> list[TokenType]:
        return [token.token_type for token in self.tokens]

    def get_token_values(self) -> list[str]:
        return [token.value for token in self.tokens]

    def get_variables(self) -> list[str]:
        return [token.value for token in self.tokens if token.is_variable()]

    def get_values(self) -> list[str]:
        return [token.value for token in self.tokens if token.is_value()]

    def get_types(self) -> list[str]:
        return [token.value for token in self.tokens if token.is_type()]

    def get_operation(self) -> str:
        operations = [token for token in self.tokens if token.is_operation()]
        return operations[0].value

    def has_function_call(self) -> bool:
        return "call" in [token.value for token in self.tokens]

    def get_right_operand(self) -> Token:
        return self.tokens[-1]

    def get_left_operand(self) -> Token:
        return self.tokens[0]

    def __str__(self):
        return [token.value for token in self.tokens]
