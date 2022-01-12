import modules.mathformulas

class clet:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    def convert(self):
        if self.type == 'int':
            self.value = int(self.value)
        elif self.type == 'str':
            self.value = str(self.value)
        elif self.type == 'bool':
            if self.value in ['true', 'True', 1, '1', True]:
                self.value = True
            else:
                self.value = False
        elif self.type == 'float':
            self.value = float(self.value)

def get_value(i, digits):
  if '.' in i:
    type = 'float'
    value = float(i)
  elif i[-1] in digits:
    type = 'int'
    value = int(i)
  elif i[0] == '#':
    type = 'str'
    value = i[1:]
  else:
    type = names[i].type
    value = names[i].value
  return type, value

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    names['true'] = clet('true', 'bool', True)
    names['false'] = clet('false', 'bool', False)

    mathsymbols = ['+', '-', '*', '/', '%']

    namests = []
    type = "int"
    symbol = '='
    mathsymbol = 'a'
    value = 0
    aftersymbol = False
    formulas = []
    t = 1
    for i in pline[1:]:
        if i in dsymbols or i == '=':
            symbol = i
            aftersymbol = True
        elif aftersymbol == False:
            namests.append(i)
        elif i in mathsymbols:
          mathsymbol = i
          a = 0
          if len(formulas) == 0:
            type, a = get_value(pline[t-1], digits)
            formulas.append(a)
          formulas.append(pline[t])
          type, a = get_value(pline[t+1], digits)
          formulas.append(a)
        else:
            type, value = get_value(i, digits)
        t += 1

    if len(formulas) > 0:
      value = modules.mathformulas.main(formulas)

    if type != 'str':
      type, value = get_value(str(value), digits)

    for i in namests:
        if symbol == '=':
            names[i] = clet(i, type, value)
        elif symbol == '+=':
            names[i] = clet(i, type, names[i].value + value)
        elif symbol == '-=':
            names[i] = clet(i, type, names[i].value - value)
        elif symbol == '*=':
            names[i] = clet(i, type, names[i].value * value)
        elif symbol == '/=':
            names[i] = clet(i, type, names[i].value / value)
        elif symbol == '%=':
            names[i] = clet(i, type, names[i].value % value)
        elif symbol == '!=':
            names[i] = clet(i, type, not value)
        elif symbol == '<<':
            names[i] = clet(i, type, names[i].value << value)
        elif symbol == '>>':
            names[i] = clet(i, type, names[i].value >> value)
        elif symbol == '++':
          names[i] = clet(i, type, names[i].value + 1)
        elif symbol == '--':
          names[i] = clet(i, type, names[i].value - 1)
        #print(i, type, value)
    return names, levels, linenum
