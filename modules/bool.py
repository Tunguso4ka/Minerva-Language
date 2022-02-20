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
    for i in pline[1:]:
      if aftersymbol == False and i in ['=', '!=']:
        symbol = i
        aftersymbol = True
      elif aftersymbol == False:
        namests.append(i)
      elif aftersymbol == True:
        if i in boolsymbols:
          formulas.append(i)
        else:
          type, a = modules.getvalue.main(i, digits, names)
          formulas.append(i)

    if len(formulas) > 0:
      value = modules.boolformulas.main(formulas)

    for i in namests:
      if symbol == '!=':
        names[i] = boolean(i, not value)
      elif symbol == '=':
        names[i] = boolean(i, value)
    return names, levels, linenum
