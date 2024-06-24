import ply.lex as lex

reservadas = {
  'ramtun':'IF',
  'lelu':'WHILE',
  'pekenum':'PRINT',
  'ka':'AND',
  'kil':'NOT',
  'kam':'OR',
}

tokens = [
'PTCOMA',
'LLAVIZQ',
'LLAVDER',
'PARIZQ',
'DOBPUNTO',
'PARDER',
'IGUAL',
'IGUALQUE',
'NIGUALQUE',
'MAS',
'MENOS',
'POR',
'DIVIDIDO',
'MENQUE',
'MAYQUE',
'MAYIGUAL',
'MENIGUAL',
'DECIMAL',
'ENTERO',
'CADENA',
'ID',
]+list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='
t_DOBPUNTO = r':'
t_MAYIGUAL = r'>='
t_MENIGUAL = r'<='
t_PRINT = r'pekenum'
t_IF = r'ramtun'
t_WHILE = r'lelu'
t_AND = r'ka'
t_OR = r'kam'
t_NOT = r'kil'

t_ignore = " \t\n"

#detecta cuando hay salto de linea
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_COMMENT(t):
  r'\#. *'
  pass

#Detecta el identificador para poder ser retornado
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  #transforma el token en mayuscula
  t.type = reservadas.get(t.value.lower(), 'ID')

  return t

#Detecta cuando es entero
def t_ENTERO(t):
  r'\d+'
  try:
    t.value = int(t.value)
  except ValueError:
    print("Integer value too large %d",t.value)
    t.value = 0
  return t

#Detecta cuando es decimal
def t_DECIMAL(t):
  r' (\d*\.\d+) | (\d+\.\d*)'
  try:
    t.value = float(t.value)
  except ValueError:
    print("Float value too large %d", t.value)
    t.value = 0
  return t

#detecta cuando hay una cadena
def t_CADENA (t):
  r'\".*?\"'
  t.value=t.value[1:-1] #remueve las comillas
  return t

#funcion que detecta errores en los tokens
def t_error(t):
  print ("Caracter Invalido '%s'"&t.value[0] )
  t.lexer.skip (1)
  return t

# instanciamos el analizador lexico
analizador = lex.lex()