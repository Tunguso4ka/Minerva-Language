forversion = "s220110.1"

class clet:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    def convert(self):
        if self.type == 'int':
            self.value = int(self.value)
        elif self.type == 'str':
            self.value = str(self.value)
        elif self.type == 'bool':
            if self.value in ['true', 'True', 1, '1', True]:
                self.value = True
            else:
                self.value = False
        elif self.type == 'float':
            self.value = float(self.value)

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    names['true'] = clet('true', 'bool', True)
    names['false'] = clet('false', 'bool', False)

    namests = []
    type = "int"
    symbol = '='
    value = 0
    aftersymbol = False
    for i in pline[1:]:
        if i in dsymbols or i == '=':
            symbol = i
            aftersymbol = True
        elif aftersymbol == False:
            namests.append(i)
        else:
            if '.' in i:
                type = 'float'
                value = float(i)
            elif i[-1] in digits:
                type = 'int'
                value = int(i)
            elif i[0] == '#':
                type = 'str'
                value = i[1:]
            else:
                type = names[i].type
                value = names[i].value


    for i in namests:
        if symbol == '=':
            names[i] = clet(i, type, value)
        elif symbol == '+=':
            names[i] = clet(i, type, names[i].value + value)
        elif symbol == '-=':
            names[i] = clet(i, type, names[i].value - value)
        elif symbol == '*=':
            names[i] = clet(i, type, names[i].value * value)
        elif symbol == '/=':
            names[i] = clet(i, type, names[i].value / value)
        elif symbol == '%=':
            names[i] = clet(i, type, names[i].value % value)
        elif symbol == '!=':
            names[i] = clet(i, type, not value)
        elif symbol == '<<':
            names[i] = clet(i, type, names[i].value << value)
        elif symbol == '>>':
            names[i] = clet(i, type, names[i].value >> value)
        #print(i, type, value)
    return names, levels, linenum
