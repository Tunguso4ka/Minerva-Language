import string, mtoken
from os.path import exists

debug = False
version = "220425.1"

def makesingleline(lines):
  line = ''
  for i in lines:
    if i[0] != '#':
      line = line + i.strip('\n')
  return line

def lex(lines):
  global string
  code = []
  cline = []
  instring = False
  line = makesingleline(lines) + ' '
  
  i = 0

  while i < len(line):
    f = line[i]

    if f == '"':
      chars, i = makechars(line, i)
      cline.append(chars)
    elif f in "1234567890":
      number, i = makenumber(line, i)
      cline.append(number)
    elif f in string.ascii_letters or f in '_':
      unknown, i = makeunknown(line, i)
      cline.append(unknown)
    elif f in "{;":
      cline.append(tokenize(value=f))
      code.append(cline)
      cline = []
    elif f in "}":
      if not cline == []:
        code.append(cline)
        cline = []
      cline.append(tokenize(value=f))
      code.append(cline)
      cline = []
    elif f in "-+":
      if line[i+1] in f"{f}=":
        cline.append(tokenize(value=line[i:i+2]))
        i+=1
      else:
        cline.append(tokenize(value=f))
    elif f in "*/><=!%":
      if line[i+1] in '=':
        cline.append(tokenize(value=line[i:i+2]))
        i+=1
      elif f == '<' and line[i+1] in '<':
        cline.append(tokenize(value=line[i:i+2]))
        i+=1
      elif f == '>' and line[i+1] in '>':
        cline.append(tokenize(value=line[i:i+2]))
        i+=1
      elif f == '/' and line[i+1] == '/' and line[i+2] == '=':
        cline.append(tokenize(value=line[i:i+3]))
        i+=2
      elif f == '/' and line[i+1] == '/':
        cline.append(tokenize(value=line[i:i+2]))
        i+=1
      else:
        cline.append(tokenize(value=f))
    elif f in "&|":
      if line[i+1] == f:
        cline.append(tokenize(value=line[i:i+2]))
        i+=1
      else:
        error(f"Only one '{f}'.")
    elif f in "()[],":
      cline.append(tokenize(value=f))

    i+=1

  if not cline == []:
    code.append(cline)

  if debug:
    print("LEXER")
    for i in code:
      line = ""
      for f in i:
        line += f"{f.type}:{str(f.value)} "
      print(line)
    print("LEXER")
  return code

def makechars(line, i):
  chars = ""
  i+=1
  while i < len(line):
    f = line[i]
    if f == '"':
      break
    else:
      chars += f
    i+=1
  return tokenize("tt_char", chars), i

def makenumber(line, i):
  number = ""
  type = 'tt_int'
  isfloat = False
  while i < len(line):
    f = line[i]
    if not f in "1234567890.":
      i-=1
      break
    else:
      if f == '.':
        isfloat = True
      number += f
      i+=1
  
  if isfloat:
    number = float(number)
    type = 'tt_float'
  else:
    number = int(number)
  return tokenize(type, number), i

def makeunknown(line, i):
  global string
  unknown = ""
  while i < len(line):
    f = line[i]
    if not f in string.ascii_letters and not f in '_.':
      i-=1
      break
    else:
      unknown += f
      i+=1
  
  return tokenize("tt_unknown", unknown), i

def tokenize(type="tt_none", value="none"):
    if type == "tt_none":
        type = mtoken.tokens[value]
    elif type == "tt_unknown":
      if exists(f'modules/{value.replace(".", "/")}.py') or value == 'use':
        type = "tt_module"
      elif value in ['toint', 'tofloat', 'tobool', 'tochar', 'true', 'false']:
        if value == 'true':
          value = True
        elif value == 'false':
          value = False
        type = mtoken.tokens[value]
    return mtoken.t(type, value)

#res = ""
#while res != "c":
#    res = input(": ")
#    a = lex(res)
#    for i in a:
#        line = ""
#        for f in i:
#            line += f"{f.type}:{str(f.value)} "
#        print(line)