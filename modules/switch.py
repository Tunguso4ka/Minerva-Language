class cswitch:
    def __init__(self, name, value, startPos, pos, do):
        self.name = name
        self.value = value
        self.startPos = startPos
        self.pos = pos
        self.do = do
        self.type = 'switch'
    def level_end(self, names, levels, linenum):
      levels.pop()
      return names, levels, linenum

def setvalue(i, digits, names):
    value = 0
    if i[0] == '#':
        value = i[1:]
    elif i[0] in digits:
        value = int(i)
    elif i in names:
        value = names[i].value
    return value

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    value = 0
    for i in pline[1:]:
        if i == '{':
            a = 0
        else:
            value = setvalue(i, digits, names)
        
    name = pline[0] + ' ' + pline[1];
    names[name] = cswitch(name, value, linenum, linenum, True)
    levels.append(name)
    return names, levels, linenum