import modules.getvalue, modules.boolformulas

class boolean:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = "bool"
    def convert(self):
        if self.value == 'true':
            self.value = True
        else:
            self.value = False

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    names['true'] = boolean('true', True)
    names['false'] = boolean('false', False)
    boolsymbols = ['==', '!=', '&&', '||', '>', '<', '<=', '>=']

    namests = []
    type = "int"
    symbol = '='
    value = 0
    aftersymbol = False
    formulas = []
    t = 1
    for i in pline[1:]:
      if aftersymbol == False and i in ['=', '!=']:
        symbol = i
        aftersymbol = True
      elif aftersymbol == False:
        namests.append(i)
      elif aftersymbol == True:
        if i in boolsymbols:
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
      value = modules.boolformulas.main(formulas)

    for i in namests:
      if symbol == '!=':
        names[i] = boolean(i, not value)
      elif symbol == '=':
        names[i] = boolean(i, value)
    return names, levels, linenum
