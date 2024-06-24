import ply.yacc as yacc
from codexFati_lex import tokens, lexer

teste = {}

def p_odio(p):
    '''odio : exp
            | saida
            | codelines
            | program
    '''
    p[0] = p[1]

def p_codeline(p):
    '''codeline : declaracao
            | atribuicao
            | saida
            | entrada
            | if_instr
            | else_instr
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


# Codigo kibado --------------------------

Variaveis = []

def indiceVar(name):
    for i, v in enumerate(Variaveis):
        if v['name'] == name:
            return i
    
    print(f"Variable with name:'{name}' doesn't exist")
    return -1

# def value(var):
#     id = existeVar(var)
#     if(id == -1):
#         print("Variable "+var+" doesn't exist")
#     else:
#         return var
#         # if(Variaveis[id]['type'] == 'value'):
#         #     return var
#         # else:
#         #     letras = modeloResitor2vetor(Variaveis[id]['value'])
#         #     return conversao1(letras)

def p_main(p):
    '''program : START codelines END'''
    print("isso é a main")
    f = open("temp.cpp", "w")
    f.write(f"#include <iostream>\n#include <string>\n\nint main(){{\n{p[2]}\n\treturn 0;\n}}")
    f.close()


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


# ----------------------------------------------------

#Definindo expressões genéricas ----------------------
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
        elif p[2] == '+':
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

# def p_while(p):
#   'while_instr : WHILE OPEN_PARENTHESIS exp CLOSE_PARENTHESIS OPEN_BRACES codeline CLOSE_BRACES'
  
#   p[0] = 
#   while(t[3]):
#     t[0]=t[6]

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

    moon(x)
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

########################################################################################


# def p_var(p):
#     '''
#         variaveis : VARIAVEL
#     '''
#     p[0] = p[1]

# def p_Variaveis(p):
#     '''
#         variaveis : variaveis VIRGULA VARIAVEL
#     '''
#     p[0] = F'{p[1]}{p[2]}{p[3]}'

# def p_definicaovalue(p):
#     '''
#         definicaovalue : VARIAVEL ATRIBUICAO value TERMINADOR_LINHA
#     '''
#     if existeVar(p[1]) == -1:
#         print("Variavel não declarada!")
#     Variaveis[existeVar(p[1])]['value'] = p[3]
#     p[0] = f'{p[1]} = {p[3]}{p[4]}'

# def p_definicaoResistor(p):
#     '''
#         definicaoResistor : VARIAVEL ATRIBUICAO modeloResistor TERMINADOR_LINHA
#     '''
#     if existeVar(p[1]) == -1:
#         print("Variavel não declarada!")
#     Variaveis[existeVar(p[1])]['value'] = p[3]
#     p[0] = f'strcpy({p[1]},"{p[3]}"){p[4]}'

# def p_modeloResisor3(p):
#     '''
#         modeloResistor : ABRE_COLCHETES cor VIRGULA cor VIRGULA cor FECHA_COLCHETES

#     '''
#     p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}{p[7]}'

# def p_modeloResisor4(p):
#     '''
#         modeloResistor : ABRE_COLCHETES cor VIRGULA cor VIRGULA cor VIRGULA cor FECHA_COLCHETES

#     '''
#     p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}{p[7]}{p[8]}{p[9]}'

# def p_Cor(p):
#     '''
#         cor : PRETO
#             | MARROM
#             | VERMELHO
#             | LARANJA
#             | AMARELO
#             | VERDE
#             | AZUL
#             | VIOLETA
#             | CINZA
#             | BRANCO
#             | DOURADO
#             | PRATEADO
#     '''
#     p[0] = p[1]
    
# def p_operacaoParalelo(p):
#     '''
#         operacaoParalelo : VARIAVEL ATRIBUICAO resParalelo TERMINADOR_LINHA
#     '''
#     id = existeVar(p[1])
#     if  id == -1:
#         print("Variavel não declarada!")
#     if Variaveis[id]['type'] != "value":
#         print("Tipo incorreto para conversao")
#     p[0] = f'{p[1]} = {p[3]}{p[4]}\n    ' 

# def p_resParalelo(p):
#     '''
#         resParalelo : VARIAVEL PARALELO VARIAVEL
#     '''
#     p[0] = f'(1.0/((1.0/{value(p[1])})+1.0/({value(p[3])})))'

# def p_resParalelo2(p):
#     '''
#         resParalelo : resParalelo PARALELO VARIAVEL
#     '''
#     p[0] = f'(1.0/((1.0/{p[1]})+1.0/({value(p[3])})))'

# def p_operacaoSerie(p):
#     '''
#         operacaoSerie : VARIAVEL ATRIBUICAO resSerie TERMINADOR_LINHA
#     '''
#     id = existeVar(p[1])
#     if  id == -1:
#         print("Variavel não declarada!")
#     if Variaveis[id]['type'] != "value":
#         print("Tipo incorreto para conversao")
#     p[0] = f'{p[1]} = {p[3]}{p[4]}\n    '

# def p_resSerie(p):
#     '''
#         resSerie : VARIAVEL SERIE VARIAVEL
#     '''
#     p[0] = f'{value(p[1])} + {value(p[3])}'

# def p_resSerie2(p):
#     '''
#         resSerie : resSerie SERIE VARIAVEL
#     '''
#     p[0] = f'{p[1]} + {value(p[3])}'

# def p_conversao1(p):
#     '''
#         conversao1 : VARIAVEL ATRIBUICAO CONVERSAO_value modeloResistor TERMINADOR_LINHA
#     '''
#     id = existeVar(p[1])
#     if  id == -1:
#         print("Variavel não declarada!")
#     if Variaveis[id]['type'] != "value":
#         print("Tipo incorreto para conversao")
#     valueRes = conversao1(modeloResitor2vetor(p[4]))
#     Variaveis[id]['value'] = valueRes
#     Variaveis[id]['type'] = 'value'
#     p[0] = f'{p[1]} = {valueRes}{p[5]}'

# def p_conversao2(p):
#     '''
#         conversao2 : VARIAVEL ATRIBUICAO CONVERSAO_RESISTOR value TERMINADOR_LINHA
#     '''
#     id = existeVar(p[1])
#     if  id == -1:
#         print("Variavel não declarada!")
#     if Variaveis[id]['type'] != "resistor":
#         print("Tipo incorreto para conversao")
#     valueRes = conversao2(float(p[4]))
#     Variaveis[id]['value'] = valueRes
#     Variaveis[id]['type'] = 'resistor'
#     p[0] = f'strcpy({p[1]},"{valueRes}"){p[5]}'

# def p_conversaoGenerica(p):
#     '''
#         conversaoGenerica : VARIAVEL ATRIBUICAO conversao VARIAVEL TERMINADOR_LINHA
#     '''
#     id = existeVar(p[1])
#     if  id == -1:
#         print("Variavel não declarada!")
#     tipo = 'value' if (p[3] == "re2va") else 'resistor'
#     if Variaveis[id]['type'] != tipo:
#         print("Tipo incorreto para conversao")
#     id = existeVar(p[4])
#     if(tipo == 'value'):
#         valueRes = conversao1(modeloResitor2vetor(Variaveis[id]['value']))
#         Variaveis[existeVar(p[1])]['value'] = valueRes
#         p[0] = f'{p[1]} = {valueRes}{p[5]}'
#     else:
#         valueRes = conversao2(float(Variaveis[id]['value']))
#         Variaveis[existeVar(p[1])]['value'] = valueRes
#         p[0] = f'strcpy({p[1]},"{valueRes}"){p[5]}'

# def p_conversao(p):
#     '''
#         conversao : CONVERSAO_RESISTOR 
#                    | CONVERSAO_value
#     '''
#     p[0] = p[1]

# def p_mostrar(p):
#     '''
#         mostrar : MOSTRAR ABRE_COLCHETES variaveis FECHA_COLCHETES TERMINADOR_LINHA
#     '''
#     Variaveis = p[3].split(',')
#     p[0] = ''
#     for v in Variaveis:
#         id = existeVar(v)
#         if(id == -1):
#             print("Variavel"+{v}+"nao existente")
#         else:
#             if(Variaveis[id]['type'] == 'value'):
#                 p[0] += f'printf("{v} = %.2f\\n",{v}){p[5]}\n   '
#             else:
#                 p[0] += f'printf("{v} = %s\\n",{v}){p[5]}\n   '

# parser = yacc.yacc()

# from exemploCodigos import interpretar

# result = parser.parse(interpretar)