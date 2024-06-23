import ply.yacc as yacc
from codexFati_lex import tokens

#Definindo expressões aritméticas###########################
def p_exp_arit(p):
    'exp_arit : term ARITOP term'
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
        
def p_termo_arit(p):
    '''term : INT  
    | FLOAT  
    | ID 
    | OPEN_PARENTHESIS exp_arit CLOSE_PARENTHESIS '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = ( p[2] )


#############################################################

#Definindo expressões lógicas################################
def p_termo_logico(p):
    '''logic_term : INT 
    | FLOAT 
    | ID 
    | CHAR 
    | STRING 
    | OPEN_PARENTHESIS exp_logica CLOSE_PARENTHESIS '''
    
    if(len(p)==2):
        p[0] = p[1]
    else:
        p[0] = ( p[2] )

def p_exp_logica(p):
    '''exp_logica : logic_term RELOP logic_term
                | logic_term AND logic_term
                | logic_term OR logic_term '''
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
    elif p[2] == 'theLovers':
        p[0] = p[1] and p[3]
    elif p[2] == 'theDevil':
        p[0] = p[1] or p[3]
    
###############################################################

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser

parser = yacc.yacc()

result = parser.parse(
    ''' 
    2

    '''
)
print(result)
