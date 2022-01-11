class function:
    def __init__(self, name, value, startPos, pos, do):
        self.name = name
        self.value = value
        self.startPos = startPos
        self.pos = pos
        self.callpos = 0
        self.do = do
        self.type = 'fn'
    def level_end(self, names, levels, linenum):
      levels.pop()
      if self.do:
        linenum = names[levels[-1]].pos
      return names, levels, linenum

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    bracket_reached = False
    fnname = 'name'
    do = True
    namests = []
    for i in pline[1:]:
        if i == '(' or i == ')':
            bracket_reached = not bracket_reached
        elif i == '{':
            do = False
        elif bracket_reached == False:
            fnname = i
        elif bracket_reached == True:
            namests.append(i)

    value = {}
    if do == False:
        for i in namests:
            value[i] = 0
    else:
        a = 0
        for i in names[fnname].value:
            i = namests[a]
            a += 1

    if do == False:
        if fnname in levels:
            levels.pop()
        names[fnname] = function(fnname, value, linenum, linenum, False)
        levels.append(fnname)
    else:
        linenum = names[fnname].startPos
        if names[levels[-1]].do == True:
          names[fnname].do = True
        levels.append(fnname)

    return names, levels, linenum
