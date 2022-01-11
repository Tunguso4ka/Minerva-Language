class string:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = "str"
    def convert(self):
        self.value = str(self.value)

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    equal_reached = False
    result = ''
    namests = []
    for i in pline[1:]:
            if i == '=':
                equal_reached = not equal_reached
            elif equal_reached == False:
                namests.append(i)
            elif equal_reached == True:
                if i[0] == '#':
                    result = i[1:]
                elif i in names:
                    result = names[i].value
            
    for i in namests:
        names[i] = string(i, result)
    return names, levels, linenum