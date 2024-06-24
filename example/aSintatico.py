from alexico import tokens, analizador
from sys import stdin
import ply.yacc as yacc

#Prioridad de tokens
precedence =(
  ('right', 'IGUAL'),
  ('right', 'IGUALQUE'),
  ('left', 'MAYQUE', 'MENQUE'), #' menor', 'menorigual'),
  ('left', 'MAS', 'MENOS'),
  ('left', 'POR', 'DIVIDIDO'),
  ('left', 'PARIZQ', 'PARDER'),
  ('left', 'LLAVIZQ', 'LLAVDER')
  )

nombres = {}

def p_init(t):
  'init : instrucciones'
  t[0] = t[1]

def p_instrucciones_lista(t) :
  'instrucciones : instrucciones instruccion'
  t[1].append(t[2])
  t[0] = t[1]

def p_instrucciones_instruccion(t):
  'instrucciones : instruccion'
  t[0]=[t[1]]

def p_instruccion(t):
  '''instruccion: imprimir_instr
                  | asignacion_instr
                  | if_instr
                  | while_instr
  '''
  t[0] = t[1]

def p_if(t):
  'if_instr: IF PARIZQ expresion_logica PARDER LLAVIZQ statement LLAVDER'
  print(t[3])
  if(t[3]):
    t[0]=t[6]

def p_statement (t):
  '''statement: imprimir_instr
                | if_instr
                | expresion
                | while_instr
  '''
  t[0] = t[1]
  print(t[0])

def p_while(t):
  'while_instr : WHILE PARIZQ expresion_logica PARDER LLAVIZQ statement LLAVDER'
  while(t[3]):
    t[0]=t[6]

#Asignacion de variables
def p_asignacion(t):
  'asignacion_instr : ID IGUAL expresion PTCOMA'
  nombres[t[1]] = t[3]

def p_asignacion_tipo(t):
  '''expresion: ENTERO
                | DECIMAL
                | CADENA
  '''
  t[0] = t[1]

def p_expresion_id(t):
  'expresion : ID'
  t[0] = nombres[t[1]]

#Funciones del lenguaje
def p_print(t):
  'imprimir_instr : PRINT PARIZQ expresion PARDER PTCOMA'
  t[0] = t[3]

def p_expresion_group(t):
  ' expresion : PARIZQ expresion PARDER '
  t[0] = t[2]

def p_expresion_logica(t):
  '''expresion_logica : expresion MENQUE expresion
                      | expresion MAYQUE expresion
                      | expresion IGUALQUE expresion
                      | expresion NIGUALQUE expresion
                      | expresion MAYIGUAL expresion
                      | expresion MENIGUAL expresion
  '''
  if t[2] == '<' : t[0] = t[1] < t[3]
  elif t[2] == '>' : t[0] = t[1] > t[3]
  elif t[2] == '==' : t[0] = t[1] == t[3]
  elif t[2] == '!=' : t[0] = t[1] != t[3]
  elif t[2] == '<=' : t[0] = t[1] <= t[3]
  elif t[2] == '>=' : t[0] = t[1] >= t[3]

def p_expresion_logica_group(t):
  'expresion_logica: PARIZQ expresion_logica PARDER'
  t[0]=t[2]

def p_expresion_logica_group(t):
  '''expresion logica : PARIZQ expresion_logica PARDER MENQUE PARIZQ expresion_logica PARDER
                      | PARIZQ expresion_logica PARDER MAYQUE PARIZQ expresion_logica PARDER
                      | PARIZQ expresion_logica PARDER IGUALQUE PARIZQ expresion_logica PARDER
                      | PARIZQ expresion_logica PARDER NIGUALQUE PARIZQ expresion_logica PARDER
                      | PARIZQ expresion logica PARDER MAYIGUAL PARIZQ expresion_logica PARDER
                      | PARIZQ expresion_logica PARDER MENIGUAL PARIZQ expresion_logica PARDER
  '''
  if t[4] == '<': t[0] = t[2] < t[5]
  elif t[4] == '>': t[0] = t[2] > t[5]
  elif t[4] == '==':t[0] = t[2] == t[5]
  elif t[4] == '!=':t[0] = t[2] != t[5]
  elif t[2] == '<=': t[0] = t[2] <= t[5]
  elif t[2] == '>=': t[0] = t[2] >= t[5]

def p_expresion_operador_logico (t):
  '''expresion logica: PARIZQ expresion_logica PARDER AND PARIZQ expresion_logica PARDER
                    | PARIZQ expresion_logica PARDER ORD PARIZQ expresion_logica PARDER
                    | PARIZQ expresion logica PARDER NOT PARIZQ expresion_logica PARDER
  '''
  if t[4] == 'ka': t[0] = t[2] and t[5]
  elif t[4] == 'kam': t[0] = [2] or t[5]
  elif t[4] == 'kil': t[0]= t[2] is not t[5]

def p_expresion_operaciones (t):
  '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIVIDIDO expresion
  '''
  if t[2] == '+': t[0] = t[1] + t[3]
  elif t[2] == '-' : t[0] = t[1] - t[3]
  elif t[2] == '*' : t[0] = t[1] * t[3]
  elif t[2] == '/': t[0] = t[1] / t[3]

def p_error(t):
  global resultado_gramatica
  if t:
    resultado =  "Error sintactico de tipo {} en el valor {}".format( str(t.type), str(t.value))
  else:
    resultado = "Error sintactico {}".format(t)

  resultado_gramatica.append(resultado)

# instanciamos el analizador sistactico
parser = yacc.yacc()
resultado_gramatica = []

def prueba (data):
  resultado_gramatica.clear()
  for item in data.splitlines():
    if item:
      gram = parser.parse(item)
    if gram:
      resultado_gramatica.append(str(gram))
  return resultado_gramatica