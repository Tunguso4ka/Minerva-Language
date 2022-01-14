import modules.mathformulas, modules.getvalue

class integer:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = "int"
    def convert(self):
        self.value = int(self.value)

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    mathsymbols = ['+', '-', '*', '/', '%']
    namests = []
    type = "int"
    symbol = '='
    mathsymbol = 'a'
    value = 0
    aftersymbol = False
    formulas = []
    t = 1
    for i in pline[1:]:
        if i in dsymbols or i == '=':
            symbol = i
            aftersymbol = True
        elif aftersymbol == False:
            namests.append(i)
        elif i in mathsymbols:
          mathsymbol = i
          a = 0
          if len(formulas) == 0:
            type, a = modules.getvalue.main(pline[t-1], digits, names)
            formulas.append(a)
          formulas.append(pline[t])
          type, a = modules.getvalue.main(pline[t+1], digits, names)
          formulas.append(a)
        else:
            type, value = modules.getvalue.main(i, digits, names)
        t += 1

    if len(formulas) > 0:
      value = modules.mathformulas.main(formulas)

    if symbol == '=':
        for i in namests:
            names[i] = integer(i, value)
    elif symbol == '++':
        for i in namests:
            names[i].value = names[i].value + 1
    elif symbol == '--':
        for i in namests:
            names[i].value = names[i].value - 1
    elif symbol == '+=':
        for i in namests:
            names[i].value = names[i].value + value
    elif symbol == '-=':
        for i in namests:
            names[i].value = names[i].value - value
    elif symbol == '*=':
        for i in namests:
            names[i].value = names[i].value * value
    elif symbol == '/=':
        for i in namests:
            names[i].value = names[i].value / value
    elif symbol == '%=':
        for i in namests:
            names[i].value = names[i].value % value
    names[i].convert()
    return names, levels, linenum
