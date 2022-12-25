from core.simplifier import Simplifier
from core.tokenizer import Tokenizer
from core.analyzer import Analyzer
from core.common.formatter import Formatter
from core.optimizers.optimizer import Optimizer
from core.transalators.functionTranslator import FunctionTranslator


def main():

    text = """
define dso_local noundef i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, ptr %1, align 4
  store i32 5, ptr %2, align 4
  store i32 4, ptr %3, align 4
  %4 = load i32, ptr %2, align 4
  %5 = load i32, ptr %3, align 4
  %6 = add nsw i32 %4, %5
  ret i32 %6
}
    """

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)

    simplifier = Simplifier()
    tokens = simplifier.simplify(tokens)

    analyzer = Analyzer()
    lines = analyzer.analyze_to_lines(tokens)
    functions = analyzer.analyze_to_functions(lines)
    translator = FunctionTranslator()
    assembler_code = translator.translate(functions)
    print(str(assembler_code))

    opt = Optimizer()
    commands = opt.optimize(assembler_code.lines_to_optimize)
    print()
    print("=========AFTER OPTIMIZATION=============")
    assembler_code = Formatter.format_commands(commands)
    print("\n".join(assembler_code))


if __name__ == "__main__":
    main()
