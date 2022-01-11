def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    result = '\033[0mout:\033[93m'
    for i in pline[1:]:
        if i[0] == '#':
            result = result + i[1:] + ' '
        elif i in names:
            result = result + str(names[i].value) + ' '
        elif i[0] in digits:
            result = result + i + ' '

    print(result,"\033[0m")
    return names, levels, linenum
