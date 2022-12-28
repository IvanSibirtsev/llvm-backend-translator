from core.simplifier import Simplifier
from core.tokenizer import Tokenizer
from core.analyzer import Analyzer
from core.common.formatter import Formatter
from core.optimizers.optimizer import Optimizer
from core.transalators.functionTranslator import FunctionTranslator
from io import Reader, Writer


def main():

    text = Reader("main.ll").read()

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)

    simplifier = Simplifier()
    tokens = simplifier.simplify(tokens)

    analyzer = Analyzer()
    lines = analyzer.analyze_to_lines(tokens)
    functions = analyzer.analyze_to_functions(lines)
    translator = FunctionTranslator()
    assembler = translator.translate(functions)
    assembler_code = Formatter.format(assembler.lines)
    Writer("main_without_optimization.ll").write(assembler_code)

    opt = Optimizer()
    commands = opt.optimize(assembler.lines_to_optimize)
    assembler_code = Formatter.format_commands(commands)

    Writer("main.ll").write(assembler_code)


if __name__ == "__main__":
    main()
