import modules.boolformulas, modules.getvalue

class iff:
    def __init__(self, name, value, startPos, pos, do):
        self.name = name
        self.value = value
        self.startPos = startPos
        self.pos = pos
        self.do = do
        self.type = 'if'
    def level_end(self, names, levels, linenum):
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

    name = pline[1] + pline[2] + pline[3];
    do = False
    if names[levels[-1]].do == True:
      do = modules.boolformulas.main(formulas);
    names[name] = iff(name, 0, linenum, linenum, do)
    levels.append(name)
    return names, levels, linenum
