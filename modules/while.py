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
      if self.do == True:
        linenum = self.startPos - 1
      levels.pop()
      return names, levels, linenum

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    boolsymbols = ['==', '!=', '&&', '||', '>', '<', '<=', '>=']
    formulas = []
    t = 1
    for i in pline[1:]:
      if i == '{':
        a = 0
      else:
        if i in boolsymbols:
          a = 0
          if len(formulas) == 0:
            type, a = modules.getvalue.main(pline[t-1], digits, names)
            formulas.append(a)
          formulas.append(pline[t])
          type, a = modules.getvalue.main(pline[t+1], digits, names)
          formulas.append(a)
      t += 1

    name = ''
    for i in pline[1:-1]:
      name += i
    do = False
    if names[levels[-1]].do == True:
      do = modules.boolformulas.main(formulas);
    names[name] = whileloop(name, 0, linenum, linenum, do)
    levels.append(name)
    return names, levels, linenum
