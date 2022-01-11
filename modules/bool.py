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

    equal_reached = False
    result = False
    namests = []
    smbl = '='
    for i in pline[1:]:
            if i == '=' or i == '!=':
                smbl = i
                equal_reached = not equal_reached
            elif equal_reached == False:
                namests.append(i)
            elif equal_reached == True:
                if i in names:
                    result = names[i].value

            if smbl == '!=':
                result = not result

    for i in namests:
        names[i] = boolean(i, result)
    if len(namests) == 0:
      a = 0
    return names, levels, linenum
