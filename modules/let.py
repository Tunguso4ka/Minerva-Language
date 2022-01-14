import modules.mathformulas, modules.getvalue, modules.boolformulas

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

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    names['true'] = clet('true', 'bool', True)
    names['false'] = clet('false', 'bool', False)
    mathsymbols = ['+', '-', '*', '/', '%']
    boolsymbols = ['==', '!=', '&&', '||', '>', '<', '<=', '>=']

    namests = []
    type = "int"
    symbol = '='
    value = 0
    aftersymbol = False
    usebool = False
    formulas = []
    t = 1
    for i in pline[1:]:
        if aftersymbol == False and (i in dsymbols or i == '='):
            symbol = i
            aftersymbol = True
        elif aftersymbol == False:
            namests.append(i)
        elif aftersymbol == True:
          if i in mathsymbols or i in boolsymbols:
            if i in boolsymbols:
              usebool = True
            a = 0
            if len(formulas) == 0:
              type, a = modules.getvalue.main(pline[t-1], digits, names)
              formulas.append(a)
            formulas.append(pline[t])
            type, a = modules.getvalue.main(pline[t+1], digits, names)
            formulas.append(a)
          else:
            type, value = modules.getvalue.main(i, digits, names)
        t += 1

    if len(formulas) > 0:
      if usebool:
        value = modules.boolformulas.main(formulas)
      else:
        value = modules.mathformulas.main(formulas)

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
            names[i] = clet(i, type, names[i].value != value)
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
