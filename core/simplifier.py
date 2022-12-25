from core.token import Token
from core.tokenType import TokenType


class Simplifier:
    def __init__(self):
        pass

    def simplify(self, tokens: list[Token]):
        i = 0
        result = []
        while i < len(tokens):
            token = tokens[i]
            if token.is_type() and tokens[i+1].token_type in [TokenType.Value, TokenType.Variable]:
                pass

            if token.is_new_line() and i + 1 < len(tokens) and tokens[i+1].is_new_line():
                result.append(token)
                i += 2
                continue

            if token.is_operation() and i + 1 < len(tokens) and tokens[i+1].is_operation():
                new_token = Token(token.value + " " + tokens[i+1].value, TokenType.Operation)
                result.append(new_token)
                i += 2
                continue

            result.append(token)
            i += 1
        return result
