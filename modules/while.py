import modules.boolformulas, modules.getvalue

class whileloop:
    def __init__(self, name, value, startPos, pos, do):
        self.name = name
        self.value = value
        self.startPos = startPos
        self.pos = pos
        self.do = do
        self.type = 'while'
    def level_end(self, names, levels, linenum):
      if self.do in [True, 'True', 'true', 1, '1']:
        linenum = self.startPos - 1
      levels.pop()
      return names, levels, linenum

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    boolsymbols = ['==', '!=', '&&', '||', '>', '<', '<=', '>=']
    formulas = []
    for i in pline[1:]:
      if i == '{':
        break
      elif i in boolsymbols:
        formulas.append(i)
      else:
        type, a = modules.getvalue.main(i, digits, names)
        formulas.append(i)

    name = ''
    for i in pline[0:-1]:
      name += i + '_'
    name = name[0:-1]
    do = False
    if names[levels[-1]].do == True:
      do = modules.boolformulas.main(formulas);
    names[name] = whileloop(name, 0, linenum, linenum, do)
    levels.append(name)
    return names, levels, linenum
