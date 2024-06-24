import ply.yacc as yacc
from codexFati_lex import tokens, lexer

Variaveis = []

# funções auxiliares 
def indiceVar(name):
    for i, v in enumerate(Variaveis):
        if v['name'] == name:
            return i
    
    print(f"Variable with name:'{name}' doesn't exist")
    return -1

# funções utilizadas pelo analisador
def p_init(p):
    '''init : codelines
            | program
    '''
    p[0] = p[1]


def p_main(p):
    '''program : START codelines END'''
    print("isso é a main")
    f = open("temp.cpp", "w")
    f.write(f"#include <iostream>\n#include <string>\n\nint main(){{\n{p[2]}\n\treturn 0;\n}}")
    f.close()


def p_codeline(p):
    '''codeline : declaracao
            | atribuicao
            | saida
            | entrada
            | if_instr
            | else_instr
            | while_instr
            | for_instr
    '''
    print("isso é codeline")
    p[0] = f"\t{p[1]}"


def p_codelines(p):
    '''codelines : codeline
            | codelines codeline'''
    if(len(p) == 2):
        p[0] = f"{p[1]}"
    else:
        p[0] = f"{p[1]}\n{p[2]}"


def p_term(p):
    '''term : INT
            | FLOAT
            | ID
            | STRING
            | CHAR
    '''
    p[0] = p[1]


def p_declaracao(p):
    '''
    declaracao : T_INT ID EQUALS INT
         | T_FLOAT ID EQUALS FLOAT
         | T_CHAR ID EQUALS CHAR
         | T_STRING ID EQUALS STRING
     '''

    if(indiceVar(p[2]) != -1):
        print(f"Variable with name:'{p[2]}' already exists")
        # parar execução
        return

    Variaveis.append({'name': p[2], 'type': p[1], 'value': p[4]})

    match(p[1]):
        case 'theKnight':
            if type(p[4]) == int:
                p[0] = f'int {p[2]} = {p[4]};'
        case 'temperance':
            if type(p[4]) == float:
                p[0] = f'float {p[2]} = {p[4]};'
        case 'death':
            if type(p[4]) == str and len(p[4]) == 3:
                p[0] = f'char {p[2]} = {p[4]};'
        case 'theHighPriestess':
            if type(p[4]) == str:
                p[0] = f'String {p[2]} = {p[4]};'


def p_atribuicao(p):
    '''
    atribuicao : ID ATTRIBUTION ID
            | ID ATTRIBUTION exp
            | ID EQUALS ID
            | ID EQUALS exp
    '''
    
    index = indiceVar(p[1])
    if(index == -1):
        # parar execução
        return

    match(p[2]):
        case '+=':
            Variaveis[index]["value"] += p[3]
            p[0] = f'{p[1]} += {p[3]};'
        case '-=':
            Variaveis[index]["value"] -= p[3]
            p[0] = f'{p[1]} -= {p[3]};'
        case '*=':
            Variaveis[index]["value"] *= p[3]
            p[0] = f'{p[1]} *= {p[3]};'
        case '/=':
            Variaveis[index]["value"] /= p[3]
            p[0] = f'{p[1]} /= {p[3]};'
        case '%=':
            Variaveis[index]["value"] %= p[3]
            p[0] = f'{p[1]} %= {p[3]};'
        case 'justice':
            Variaveis[index]["value"] = p[3]
            p[0] = f'{p[1]} = {p[3]};'


def p_generic_expression(p):
    '''exp : term
                | OPEN_PARENTHESIS exp CLOSE_PARENTHESIS
                | exp RELOP exp
                | exp ARITOP exp
                | exp AND exp
                | exp OR exp
                | NOT exp
                ''' 
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = f"!{p[2]}"
    elif(len(p) == 4):
        if p[2] == '==':
            p[0] = f"{p[1]} == {p[3]}"
        elif p[2] == '>=':
            p[0] = f"{p[1]} >= {p[3]}"
        elif p[2] == '<=':
            p[0] = f"{p[1]} <= {p[3]}"
        elif p[2] == '>':
            p[0] = f"{p[1]} > {p[3]}"
        elif p[2] == '<':
            p[0] = f"{p[1]} < {p[3]}"
        elif p[2] == '!=':
            p[0] = f"{p[1]} != {p[3]}"
        elif p[2] == 'AND':
            p[0] = f"{p[1]} && {p[3]}"
        elif p[2] == 'OR':
            p[0] = f"{p[1]} || {p[3]}"
        elif p[2] == '+':
            p[0] = f"{p[1]} + {p[3]}"
        elif p[2] == '-':
            p[0] = f"{p[1]} - {p[3]}"
        elif p[2] == '*':
            p[0] = f"{p[1]} * {p[3]}"
        elif p[2] == '/':
            p[0] = f"{p[1]} / {p[3]}"
        elif p[2] == '%':
            p[0] = f"{p[1]} % {p[3]}"
        elif p[1] == '(':
            p[0] = f"({p[2]})"


def p_if(p):
    'if_instr : IF OPEN_PARENTHESIS exp CLOSE_PARENTHESIS OPEN_BRACES codeline CLOSE_BRACES'

    p[0] = f'''
        if({p[3]}) {{
            {p[6]}
        }}
    '''


def p_else(p):
    'else_instr : if_instr ELSE OPEN_BRACES codeline CLOSE_BRACES'
    
    p[0] = f'''
        {p[1]} 
        else {{
            {p[4]}
        }}
    '''


def p_while(p):
  'while_instr : WHILE OPEN_PARENTHESIS exp CLOSE_PARENTHESIS OPEN_BRACES codeline CLOSE_BRACES'

  p[0] = f'''
    while({p[3]}){{
        {p[6]}
    }}
  '''

def p_for(p):
    'for_instr : FOR OPEN_PARENTHESIS exp SEMICOLON exp SEMICOLON exp CLOSE_PARENTHESIS OPEN_BRACES codeline CLOSE_BRACES'
    print('aqui',p[3])
    p[0] = f'''
        for({p[3]}; {p[5]}; {p[7]}){{
            {p[10]}
        }}
    '''

def p_print(p):
    '''
        saida : OUTPUT OPEN_PARENTHESIS ID CLOSE_PARENTHESIS
    '''
    p[0] = f'std::cout << {p[3]};'


def p_read(p):
    '''
    entrada : INPUT OPEN_PARENTHESIS ID CLOSE_PARENTHESIS
    '''
    p[0] = f'std::cin << {p[3]};'


# # Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")


code = ''' 
start
    theKnight y justice 5
    theKnight x justice 10

    hermit(theKnight x justice 0; x < y; x += 1){
        sun(x)
    }

end
'''


# Build the parser
parser = yacc.yacc()

#Dar input para o lexer
lexer.input(code)

#Tokenizar
while True:
    tok = lexer.token()
    if not tok: #Se não tiver mais input
        break  
    print(tok)

result = parser.parse(code)
print(result)

print(f"Variaveis: {Variaveis}")
