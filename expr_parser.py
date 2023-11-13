import ply.yacc as yacc
from lexer import tokens  # Импорт токенов из лексера

# Импортируем классы для AST из файла ast_nodes.py
from ast_nodes import NumNode, BinOpNode

# Правила грамматики и построение AST

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    p[0] = BinOpNode(p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = NumNode(p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Создание парсера
parser = yacc.yacc()
