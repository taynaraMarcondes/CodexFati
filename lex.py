import ply.lex as lex
from ply.lex import TOKEN

reserved = {
    'theKnight':'INT',
    'temperance':'FLOAT',
    'death':'CHAR',
    'theHighPriestess':'STRING',
    'moon':'INPUT',
    'sun':'OUTPUT',
    'magician':'IF',
    'wheelOfFortune':'ELSE',
    'emperor':'WHILE',
    'hermit':'FOR',
    'justice':'EQUALS',
    'theChariot':'RETURN',
    'theLovers':'AND',
    'theDevil':'OR',
    'theTower':'NOT',
} 

tokens = [
    'DECLARATION',
    'ATTRIBUTION',
    'ID',
    'ARITEXP',
    'ARITOP',
    'LOGEXP',
    'LOGOP',
    'RELOP',
    'DOT',
    'COMMA',
    'SEMICOLON',
    'OPEN_BRACES',
    'OPEN_PARENTHESIS',
    'CLOSE_BRACES',
    'CLOSE_PARENTHESIS',
] + list(reserved.values())


t_DOT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'
t_OPEN_BRACES = r'{'
t_OPEN_PARENTHESIS = r'\('
t_CLOSE_BRACES = r'}'
t_CLOSE_PARENTHESIS = r'\)'
t_ARITOP = r'\+|-|\*|/|%'
t_RELOP = r'==|>=|<=|>|<|!='
t_ATTRIBUTION = r'justice|\+=|-=|\*=|/=|%='
t_DECLARATION = r'justice|\+=|-=|\*=|/=|%='
t_EQUALS = r'='
t_STRING = r"\"[^'()]*\""
t_CHAR = r"'[^'()]'"

#Acho que tem que usar o @TOKEN e esse tipo de declaração pra fazer as equações lá
digit = r'[0-9]'
letter = r'[A-Za-z]'
symbol = r'[a-zA-Z_0-9]'
operator = r'+|-|*|/|%'
identifier = letter + r'(' + symbol + r')*'
##################################################################################

def t_FLOAT(t):
    r'[0-9]+(.[0-9]+)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t


#Regra para ignorar espaços
t_ignore  = ' \t'

#Regra para dar mensagem de herro caso haja caracteres que não têm token atribuido
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Regra para contar o número de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Constrói o lexer
lexer = lex.lex()

#Código para teste
data = '''
theKnight op justice 1
    temperance value

    emperor(op != 0){
        sun("digite um numero real:\n")
        moon(value)

        sun("qual opcao deseja:\n")
        sun("0 - sair\n")
        sun("1 - somar 5.50\n")
        sun("2 - subtrair 3.50\n")
        moon(op)
        
        magician(op == 1) {
            value justice value + 5.5
            sun(value)
        } wheelOfFortune magician(op == 2){
            value justice value - 3.5
            sun(value)
        } wheelofFortune {
            sun("Opcao invalida\n")
        }
    }
'''

#Dar para o lexer input
lexer.input(data)

#Tokenizar
while True:
    tok = lexer.token()
    if not tok: #Se não tiver mais input
        break  
    print(tok)