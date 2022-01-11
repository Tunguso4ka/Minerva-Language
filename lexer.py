version = "220110.1"

def makesingleline(lines):
  line = ''
  #print(lines)
  for i in lines:
    line = line + i.strip('\n')
  #print(line)
  return line

def lex(lines, digits, symbols, dsymbols):
  code = []
  cline = ['']
  instring = False
  endsymbolreached = False
  line = makesingleline(lines)
  #print(line)
  #for cycle that go throught line
  for i in line:
    #if i == " then this string
    if i == '"':
      instring = not instring
      if instring:
        cline[-1] = '#'
    #
    elif instring:
      cline[-1] = cline[-1] + i
    # if ; then end of the cline
    elif i in [';']:
      endsymbolreached = True
      if cline[-1] == '':
        cline.pop()
      code.append(cline)
      cline = ['']
    #if { then end of the cline
    elif i in ['{']:
      endsymbolreached = True
      if cline[-1] == '':
        cline[-1] = i
      else:
        cline.append(i)
      code.append(cline)
      cline = ['']
    #if } then end of cline
    elif i in ['}']:
      endsymbolreached = True
      if cline[0] == '':
        cline[0] = i
        code.append(cline)
      elif cline[-1] == '':
        cline.pop()
        code.append(cline)
        code.append([i])
      cline = ['']
    #if space then new word
    elif i == ' ':
      if cline[-1] != '':
        cline.append('')
    #if i in symbols then check for dsymbols and add
    elif i in symbols:
      if cline[-2] in symbols:
        if cline[-2] + i in dsymbols:
          cline[-2] = cline[-2] + i
        else:
          cline[-1] = i
          cline.append('')
      elif cline[-1] == '':
        cline[-1] = i
        cline.append('')
      else:
        cline.append(i)
        cline.append('')
    #if i in digits then check for digits and add
    elif i in digits:
      if cline[-2][-1] in digits or cline[-2] == '-':
        cline[-2] = cline[-2] + i
      elif cline[-1] == '':
        cline[-1] = i
        cline.append('')
      else:
        cline.append(i)
        cline.append('')
    #add new symbol
    else:
      cline[-1] = cline[-1] + i
  if endsymbolreached == False:
    print("\033[91mtype:lexer name:lexer pos:0 'No ';' '{' or '}' symbols' \033[0m")
  #print(code)
  return code
