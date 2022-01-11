def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    result = 0
    for i in pline[1:]:
        if i in digits:
          result = int(i)
        elif i in names:
          result = names[i].value
    linenum = result
    return names, levels, linenum
