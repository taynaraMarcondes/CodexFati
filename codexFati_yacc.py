import ply.yacc as yacc
from codexFati_lex import tokens

teste = {}

def p_odio(p):
    '''odio : exp_arit
            | exp_logica
            | atribuicao
            | saida
    '''
    p[0] = p[1]

def p_termo(p):
    '''termo : INT
            | FLOAT
            | ID
    '''
    p[0] = p[1]


# Definindo expressões aritméticas --------------------------
def p_exp_arit(p):
    '''exp_arit : termo
                | exp_arit ARITOP exp_arit
                | OPEN_PARENTHESIS exp_arit CLOSE_PARENTHESIS
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '%':
            p[0] = p[1] % p[3]
        elif p[1] == '(':
            p[0] = ( p[2] )
#------------------------------------------------------------

#Definindo expressões lógicas -------------------------------

def p_exp_logica(p):
    '''exp_logica : termo
                | CHAR 
                | STRING 
                | OPEN_PARENTHESIS exp_logica CLOSE_PARENTHESIS
                | exp_logica RELOP exp_logica
                | exp_logica AND exp_logica
                | exp_logica OR exp_logica 
                | NOT exp_logica''' 
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = not p[2]
    elif(len(p) == 4):
        if p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
        elif p[2] == 'AND':
            p[0] = p[1] and p[3]
        elif p[2] == 'OR':
            p[0] = p[1] or p[3]
        elif p[1] == '(':
            p[0] = ( p[2] )
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
    atribuicao : ID ATTRIBUTION ID
        | ID ATTRIBUTION exp_arit
        | ID ATTRIBUTION exp_logica
        | ID EQUALS ID
        | ID EQUALS exp_arit
        | ID EQUALS exp_logica
    '''

    match(p[1]):
        case '+=':
            p[0] = f'{p[1]} = {p[1]} + {p[3]}'
        case '-=':
            p[0] = f'{p[1]} = {p[1]} - {p[3]}'
        case '*=':
            p[0] = f'{p[1]} = {p[1]} * {p[3]}'
        case '/=':
            p[0] = f'{p[1]} = {p[1]} / {p[3]}'
        case '%=':
            p[0] = f'{p[1]} = {p[1]} % {p[3]}'
        case 'justice':
            teste[p[1]] = p[3]


def p_print(p):
    '''
    saida : OUTPUT OPEN_PARENTHESIS exp_logica CLOSE_PARENTHESIS 
        | OUTPUT OPEN_PARENTHESIS exp_arit CLOSE_PARENTHESIS 
    '''
    p[0] = p[3]


# # Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")

# Build the parser

parser = yacc.yacc()

result = parser.parse(
    ''' 
    x justice 2
    sun(x)
    '''
)
print(result)
