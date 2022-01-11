class integer:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = "int"
    def convert(self):
        self.value = int(self.value)

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    equal_reached = False
    result = 0
    namests = []
    csmbls = ['=', '++', '--', '+=', '-=', '*=', '/=', '%=']
    smbl = '='
    for i in pline[1:]:
            if i in csmbls:
                smbl = i
                equal_reached = not equal_reached
            elif equal_reached == False:
                namests.append(i)
            elif equal_reached == True:
                if i[-1] in digits:
                    result = int(i)
                elif i in names:
                    result = names[i].value
    if smbl == '=':
        for i in namests:
            names[i] = integer(i, result)
    elif smbl == '++':
        for i in namests:
            names[i].value = names[i].value + 1
    elif smbl == '--':
        for i in namests:
            names[i].value = names[i].value - 1
    elif smbl == '+=':
        for i in namests:
            names[i].value = names[i].value + result
    elif smbl == '-=':
        for i in namests:
            names[i].value = names[i].value - result
    elif smbl == '*=':
        for i in namests:
            names[i].value = names[i].value * result
    elif smbl == '/=':
        for i in namests:
            names[i].value = names[i].value / result
    elif smbl == '%=':
        for i in namests:
            names[i].value = names[i].value % result

    return names, levels, linenum
