import ply.yacc as yacc
from codexFati_lex import tokens, lexer

variables = []

# funções auxiliares 
def varIndex(name):
    for i, v in enumerate(variables):
        if v == name:
            return i
    return -1

# funções utilizadas pelo analisador
def p_init(p):
    '''init : codelines
            | program
    '''
    p[0] = p[1]


def p_main(p):
    '''program : START codelines END'''
    f = open("temp.cpp", "w")
    f.write(f"#include <iostream>\n#include <string>\n\nint main(){{\n{p[2]}\n\treturn 0;\n}}")
    f.close()


def p_codeline(p):
    '''codeline : declaration
                | attribution
                | output
                | input
                | if_statement
                | else_statement
                | while_statement
                | for_statement
    '''
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


def p_declaration(p):
    '''
    declaration : T_INT ID EQUALS INT
                | T_FLOAT ID EQUALS FLOAT
                | T_CHAR ID EQUALS CHAR
                | T_STRING ID EQUALS STRING
     '''

    if(varIndex(p[2]) != -1):
        print(f"Variable with name:'{p[2]}' already exists")
        raise SyntaxError
        return

    variables.append(p[2])

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


def p_attribution(p):
    '''
    attribution : ID ATTRIBUTION ID
                | ID ATTRIBUTION exp
                | ID EQUALS ID
                | ID EQUALS exp
    '''
    
    index = varIndex(p[1])
    if(index == -1):
        print(f"Variable with name:'{p[2]}' doesn't exist")
        raise SyntaxError
        return

    match(p[2]):
        case '+=':
            p[0] = f'{p[1]} += {p[3]};'
        case '-=':
            p[0] = f'{p[1]} -= {p[3]};'
        case '*=':
            p[0] = f'{p[1]} *= {p[3]};'
        case '/=':
            p[0] = f'{p[1]} /= {p[3]};'
        case '%=':
            p[0] = f'{p[1]} %= {p[3]};'
        case 'justice':
            p[0] = f'{p[1]} = {p[3]};'


def p_expression(p):
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
    'if_statement : IF OPEN_PARENTHESIS exp CLOSE_PARENTHESIS OPEN_BRACES codelines CLOSE_BRACES'

    p[0] = f"if({p[3]}){{\n{p[6]}\n\t}}"


def p_else(p):
    'else_statement : if_statement ELSE OPEN_BRACES codelines CLOSE_BRACES'
    
    p[0] = f"{p[1]} else {{\n{p[4]}\n\t}}"


def p_while(p):
    'while_statement : WHILE OPEN_PARENTHESIS exp CLOSE_PARENTHESIS OPEN_BRACES codelines CLOSE_BRACES'
    
    p[0] = f"while({p[3]}){{\n{p[6]}\n\t}}"

def p_for(p):
    'for_statement : FOR OPEN_PARENTHESIS attribution SEMICOLON exp SEMICOLON attribution CLOSE_PARENTHESIS OPEN_BRACES codelines CLOSE_BRACES'
    p[0] = f"for({p[3].replace(";", "")}; {p[5]}; {p[7].replace(";", "")}){{\n{p[10]}\n\t}}"

def p_print(p):
    '''output : OUTPUT OPEN_PARENTHESIS ID CLOSE_PARENTHESIS
            | OUTPUT OPEN_PARENTHESIS term CLOSE_PARENTHESIS'''
    
    p[0] = f'std::cout << {p[3]};'


def p_read(p):
    'input : INPUT OPEN_PARENTHESIS ID CLOSE_PARENTHESIS'
    
    p[0] = f'std::cin << {p[3]};'


code = '''
start
    theKnight op justice 1
    temperance value justice 0.0
    emperor(op != 0){
        sun("digite um numero real:")
        moon(value)
        sun("qual opcao deseja:")
        sun("0 - sair")
        sun("1 - somar 5.50")
        sun("2 - subtrair 3.50")
        moon(op)
        magician(op == 1) {
            value justice value + 5.5
            sun(value)
        } wheelOfFortune {
            magician(op == 2){
                value justice value - 3.5
                sun(value)
            } wheelOfFortune {
                sun("Opcao invalida")
            }
        }
    }
end
'''
        # } wheelofFortune {
        #     sun("Opcao invalida\n")
        # }


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

print(f"variables: {variables}")
