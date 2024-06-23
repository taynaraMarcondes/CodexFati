import ply.lex as lex

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
    'ATTRIBUTION',
    'ID',
    'ARITEXP',
    'ARITOP',
    'LOGEXP',
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
t_ATTRIBUTION = r'\+=|-=|\*=|/=|%='
t_STRING = r"\"[^'\"]*\""
t_CHAR = r"'[^'\"]'"

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

#Regra para ignorar espaços e quebras de linha
t_ignore  = ' \n\t'

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
data1 = '''
batata theLovers 2
'''

#Dar input para o lexer
lexer.input(data1)

#Tokenizar
while True:
    tok = lexer.token()
    if not tok: #Se não tiver mais input
        break  
    print(tok)