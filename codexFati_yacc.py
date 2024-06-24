import ply.yacc as yacc
from codexFati_lex import tokens

teste = {}
precedence =(
  ('right', 'EQUALS'),
#   ('right', 'IGUALQUE'),
#   ('left', 'MAYQUE', 'MENQUE'), #' menor', 'menorigual'),
#   ('left', 'MAS', 'MENOS'),
#   ('left', 'POR', 'DIVIDIDO'),
  ('left', 'OPEN_PARENTHESIS', 'CLOSE_PARENTHESIS'),
  ('left', 'OPEN_BRACES', 'CLOSE_BRACES')
  )

def p_init(p):
    'init : intrucoes'
    p[0] = p[1]

def p_intrucoes_lista(p):
    '''
        intrucoes : intrucoes instrucao
                | instrucao
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

# def p_instrucoes_instrucao(p):
#     'instrucoes : instrucao'
#     p[0] = [p[1]]

def p_instrucao(p):
    '''
        instrucao : saida
                | atribuicao
    '''

# def p_odio(p):
#     '''odio : saida
#             | exp_arit
#             | exp_logica
#             | atribuicao
#     '''
#     p[0] = p[1]

def p_termo(p):
    '''termo : INT
            | FLOAT
            | CHAR
            | STRING
    '''
    p[0] = p[1]

def p_termo_id(p):
    'termo : ID'

    p[0] = teste[p[1]]

def p_termo_grupo(p):
    'termo : OPEN_PARENTHESIS termo CLOSE_PARENTHESIS'

    p[0] = p[2]

# # Definindo expressões aritméticas --------------------------
# def p_exp_arit(p):
#     '''exp_arit : termo
#                 | exp_arit ARITOP exp_arit
#                 | OPEN_PARENTHESIS exp_arit CLOSE_PARENTHESIS
#     '''
#     if(len(p) == 2):
#         p[0] = p[1]
#     elif(len(p) == 4):
#         if p[2] == '+':
#             p[0] = p[1] + p[3]
#         elif p[2] == '-':
#             p[0] = p[1] - p[3]
#         elif p[2] == '*':
#             p[0] = p[1] * p[3]
#         elif p[2] == '/':
#             p[0] = p[1] / p[3]
#         elif p[2] == '%':
#             p[0] = p[1] % p[3]
#         elif p[1] == '(':
#             p[0] = ( p[2] )
# #------------------------------------------------------------

# #Definindo expressões lógicas -------------------------------

# def p_exp_logica(p):
#     '''
#         exp_logica : termo
#                 | OPEN_PARENTHESIS exp_logica CLOSE_PARENTHESIS
#                 | exp_logica RELOP exp_logica
#                 | exp_logica AND exp_logica
#                 | exp_logica OR exp_logica 
#                 | NOT exp_logica
#     ''' 
#     if(len(p)==2):
#         p[0] = p[1]
#     elif(len(p) == 3):
#         p[0] = not p[2]
#     elif(len(p) == 4):
#         if p[2] == '==':
#             p[0] = p[1] == p[3]
#         elif p[2] == '>=':
#             p[0] = p[1] >= p[3]
#         elif p[2] == '<=':
#             p[0] = p[1] <= p[3]
#         elif p[2] == '>':
#             p[0] = p[1] > p[3]
#         elif p[2] == '<':
#             p[0] = p[1] < p[3]
#         elif p[2] == '!=':
#             p[0] = p[1] != p[3]
#         elif p[2] == 'theLovers':
#             p[0] = p[1] and p[3]
#         elif p[2] == 'theDevil':
#             p[0] = p[1] or p[3]
#         elif p[1] == '(':
#             p[0] = ( p[2] )
#------------------------------------------------------------


# def p_declaracao(p):
#     '''
#     declaracao : T_INT ID EQUALS INT
#         | T_FLOAT ID EQUALS FLOAT
#         | T_CHAR ID EQUALS CHAR
#         | T_STRING ID EQUALS STRING
#     '''

#     match(p[1]):
#         case 'theKnight':
#             if type(p[4]) == int:
#                 p[0] = f'{p[2]} = {p[4]}'
#         case 'temperance':
#             if type(p[4]) == float:
#                 p[0] = f'{p[2]} = {p[4]}'
#         case 'death':
#             if type(p[4]) == str and len(p[4]) == 1:
#                 p[0] = f'{p[2]} = {p[4]}'
#         case 'theHighPriestess':
#             if type(p[4]) == str:
#                 p[0] = f'{p[2]} = {p[4]}'

def p_atribuicao(p):
    '''
    atribuicao : ID ATTRIBUTION termo
            | ID EQUALS termo
    '''

    match(p[2]):
        case '+=':
            teste[p[1]] = teste[p[1]] + p[3]
        case '-=':
            teste[p[1]] = teste[p[1]] - p[3]
        case '*=':
            teste[p[1]] = teste[p[1]] * p[3]
        case '/=':
            teste[p[1]] = teste[p[1]] / p[3]
        case '%=':
            teste[p[1]] = teste[p[1]] % p[3]
        case 'justice':
            teste[p[1]] = p[3]
    


def p_print(p):
    'saida : OUTPUT OPEN_PARENTHESIS termo CLOSE_PARENTHESIS '
    p[0] = print(p[3])


# # Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")

# Build the parser

parser = yacc.yacc()

result = parser.parse(
    ''' 
    x justice 2
    x += 2
    sun(x)
    '''
)
print(result)
