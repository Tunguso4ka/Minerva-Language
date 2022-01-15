import modules.getvalue
from time import sleep as tsleep
def main(pline, names, digits, symbols, dsymbols, levels, linenum):
  result = '\033[0mout:\033[93m'
  for i in pline[1:]:
    type, value = modules.getvalue.main(i, digits, names)

  tsleep(value)
  return names, levels, linenum
