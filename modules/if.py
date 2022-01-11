import modules.boolformulas

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
    csmbls = ['==', '<=', '>=', '>', '<', '!=', '&&', '||']
    smbl_reached = False
    smbl = '=='
    fvalue = 0
    svalue = 0
    for i in pline[1:]:
        if i in csmbls:
            smbl = i
            smbl_reached = not smbl_reached
        elif i == '{':
            a = 0
        elif smbl_reached == False:
            fvalue = setvalue(i, digits, names)
        elif smbl_reached == True:
            svalue = setvalue(i, digits, names)
    name = pline[1] + pline[2] + pline[3];
    do = False
    if names[levels[-1]].do == True:
      do = modules.boolformulas.main([fvalue, smbl, svalue]);
    names[name] = iff(name, 0, linenum, linenum, do)
    levels.append(name)
    return names, levels, linenum