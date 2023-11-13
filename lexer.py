import ply.lex as lex

# Список токенов
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
)

# Регулярные выражения для токенов
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER   = r'\^'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Числовой токен
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Правила игнорирования пробелов
t_ignore  = ' \t'

# Обработка ошибок
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Создание лексера
lexer = lex.lex()
