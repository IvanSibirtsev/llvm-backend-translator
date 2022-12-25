class Registers:
    registers_count = 1

    def __init__(self):
        self.registers = {}
        self.variables = {}
        self._shift = 0
        self._suffix = ""

    def get_register_name_or_create_new(self, variable: str) -> str:
        if variable + self._suffix in self.variables.keys():
            return self.get_register_name_by_variable(variable)
        return self.get_new_register_name()

    def get_new_register_name(self) -> str:
        name = f"r{self.registers_count + self._shift}"
        self.registers_count += 1
        self.registers[name] = 0
        return name

    def set_variable_to_register(self, register_name: str, variable: str):
        self.registers[register_name] = variable + self._suffix
        self.variables[variable + self._suffix] = register_name

    def get_register_name_by_variable(self, variable: str) -> str:
        return self.variables[variable + self._suffix]

    def shift(self, shift: int):
        self._shift += shift

    def set_suffix(self, suffix: str):
        self._suffix = "__" + suffix

    def has_variable(self, variable: str) -> bool:
        return variable + self._suffix in self.variables.keys()

    @property
    def count(self) -> int:
        return len(self.registers)
