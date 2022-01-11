def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    namests = []
    for i in pline[1:]:
        namests.append(i)
    result = input('\033[0min: \033[93m')
    for i in namests:
        names[i].value = result
        names[i].convert()
    return names, levels, linenum
