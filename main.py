from lexer import lexer
from expr_parser import parser
from visualize import render_ast

# Тестовое арифметическое выражение
expression = "3 + 4 * (2 - 1) ^ 2 / 2"

# Лексический анализ
lexer.input(expression)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Синтаксический анализ и построение AST
ast = parser.parse(expression)

# Вывод результатов
print("Вычисленное значение:", ast.evaluate())
print("Сгенерированный код:", ast.generate_code())

# Визуализация AST
render_ast(ast, 'ast')
