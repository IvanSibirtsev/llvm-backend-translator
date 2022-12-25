import enum


class TokenType(enum.Enum):
    Variable = 1,
    Assignment = 2,
    Type = 3,
    Value = 4,
    New_Line = 5
    Operation = 6
    Label = 7
    Unknown = 8
    Memory_Access = 9
    Transfer = 10
    Function_Declaration = 11


class Semantic(enum.Enum):
    DECLARATION = 0,
    ASSIGNMENT = 1,
    CALCULATION = 2
    FUNCTION_DECLARATION = 3
    TRANSFER = 4


class Details:
    Constant_Assignment = 0
    Variable_Assignment = 1
    No = 3
