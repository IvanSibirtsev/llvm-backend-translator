from core.token import Token
from core.tokenType import TokenType as TT
from config import LLVM_OPERATIONS, LLVM_TYPES, MEMORY_ACCESS, LLVM_TRANSFER


class Tokenizer:
    def __init__(self):
        pass

    def tokenize(self, text: str) -> list[Token]:
        raw_tokens = self._prepare_text(text)
        tokens = []

        for raw_token in raw_tokens:
            if raw_token == "":
                continue

            token_type = self._define_token(raw_token)
            token = Token(raw_token, token_type)
            tokens.append(token)

        return tokens

    def _define_token(self, raw_token: str) -> TT:
        if raw_token.startswith("%"):
            return TT.Variable

        if raw_token.startswith("define"):
            return TT.Function_Declaration

        if raw_token == "=":
            return TT.Assignment

        if raw_token in LLVM_TYPES:
            return TT.Type

        if raw_token == "\n":
            return TT.New_Line

        if raw_token in LLVM_OPERATIONS:
            return TT.Operation

        if raw_token in MEMORY_ACCESS:
            return TT.Memory_Access

        if ":" in raw_token:
            return TT.Label

        if raw_token in LLVM_TRANSFER:
            return TT.Transfer

        return TT.Value

    def _prepare_text(self, text: str) -> list[str]:
        lines = text.split("\n")
        result = []
        for line in lines:
            chunks = line.split(",")
            for chunk in chunks:

                chunk = chunk.replace(")", "").replace("(", "").replace("{", "")

                if chunk == "":
                    continue

                if "align" in chunk:
                    continue

                if ";" in chunk:
                    index = chunk.index(";")
                    chunk = chunk[0:index]

                tokens = chunk.split()
                result.extend(tokens)
            result.append("\n")

        for token in result:
            token.strip()

        return result
