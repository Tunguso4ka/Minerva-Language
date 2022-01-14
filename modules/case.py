import modules.boolformulas, modules.getvalue

class ccase:
    def __init__(self, name, value, startPos, pos, do):
        self.name = name
        self.value = value
        self.startPos = startPos
        self.pos = pos
        self.do = do
        self.type = 'case'
    def level_end(self, names, levels, linenum):
      levels.pop()
      return names, levels, linenum

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    value = 0
    for i in pline[1:]:
      if i == '{':
        a = 0
      else:
        type, value = modules.getvalue.main(i, digits, names)

    name = pline[0] + ' ' + pline[1]
    do = False
    if names[levels[-1]].do == True:
      do = modules.boolformulas.main([names[levels[-1]].value, '==', value]);
    names[name] = ccase(name, value, linenum, linenum, do)
    levels.append(name)
    return names, levels, linenum
