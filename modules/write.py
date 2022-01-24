import modules.getvalue

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    result = '\033[0mout:\033[93m'
    for i in pline[1:]:
        type, value = modules.getvalue.main(i, digits, names)
        result = result + str(value) + ' '

    print(result,"\033[0m")
    return names, levels, linenum
