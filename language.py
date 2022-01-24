import lexer
from datetime import datetime
#ints
linenum = 0
#strings
version = "220124.1"
digits = '0123456789.'
symbols = '+-*/!%<>=():&|'
#bools
debug = False
stop = False
#dicts
modules = {}
names = {}
#lists
levels = []
dsymbols = ['++', '--', '+=', '-=', '==', '*=', '//', '/=', '>=', '<=', '!=', '%=', '&&','||', '<<', '>>']
#code class
class ccode:
  def __init__(self, name, startPos, pos):
    self.name = name
    self.value = 0
    self.startPos = startPos
    self.pos = pos
    self.do = True
    self.type = 'code'
  def level_end(self, names, levels, linenum):
    show_error(names[levels[-1]], 'error"Trying to end code":}')
    return names, levels, linenum
class template:
  def __init__(self, name, startPos, pos):
    self.name = name
    self.value = 0
    self.startPos = startPos
    self.pos = pos
    self.do = False
    self.type = 'code'
  def level_end(self, names, levels, linenum):
    levels.pop()
    return names, levels, linenum
#
def show_error(module, code):
  print(f"\033[91mtype:{module.type} name:{module.name} pos:{module.pos} {code} \033[0m")
#
def add_code():
  names['code'] = ccode('code', 0, linenum)
  levels.append('code')
add_code()
#
def update_pos():
  global names
  names[levels[-1]].pos = linenum
#
def execute_line(line):
  global modules, names, levels, linenum
  if line[0] == 'use':
    for i in line[1:]:
      modules[i] = __import__('modules.' + i, fromlist = [' '])
  elif line[0] == '}':
    names, levels, linenum = names[levels[-1]].level_end(names, levels, linenum)
  elif line[0][0] == '#':
    a = 0
  elif line[0] in modules:
    if names[levels[-1]].do:
      names, levels, linenum = modules[line[0]].main(line, names, digits, symbols, dsymbols, levels, linenum)
    elif line[-1] == '{':
      names['template'] = template('template', 0, linenum)
      levels.append('template')
  else:
    show_error(names[levels[-1]], f'error"Unknown module":{line[0]}')
#
def code_proccess(code):
  global linenum
  time_start = datetime.now()
  #application starts
  while linenum != len(code) and stop == False:
    execute_line(code[linenum])
    #print(code[linenum])
    linenum += 1
    update_pos()
    if debug == True:
      print('\033[0m')
      poss = ''
      for i in levels:
        poss += " " + str(names[i].pos)
      print(levels, poss)
  #application ends
  time_end = datetime.now()
  secondsgone = time_end - time_start
  if debug:
    print("\033[92m$ml Finished in", secondsgone, "\033[0m")
#
def lex(line):
  code = lexer.lex([line], digits, symbols, dsymbols)
  #print(code)
  code_proccess(code)
#
def run_file(path):
  f = open(path)
  lines = f.readlines()
  f.close()
  code = lexer.lex(lines, digits, symbols, dsymbols)
  if debug:
    a = 0
    for i in code:
      print(a, i)
      a += 1
  code_proccess(code)
