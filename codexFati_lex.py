import ply.lex as lex

reserved = {
    'theKnight':'T_INT',
    'temperance':'T_FLOAT',
    'death':'T_CHAR',
    'judgment':'T_BOOL',
    'theHighPriestess':'T_STRING',
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
    'start':'START',
    'end':'END'
} 

tokens = [
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'BOOL',
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
t_BOOL = r"true|false"
t_T_INT = r'theKnight'
t_T_FLOAT = r'temperance'
t_T_CHAR = r'death'
t_T_STRING = r'theHighPriestess'
t_INPUT = r'moon'
t_OUTPUT = r'sun'
t_IF = r'magician'
t_ELSE = r'wheelOfFortune'
t_WHILE = r'emperor'
t_FOR = r'hermit'
t_EQUALS = r'justice'
t_RETURN = r'theChariot'
t_AND = r'theLovers'
t_OR = r'theDevil'
t_NOT = r'theTower'

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