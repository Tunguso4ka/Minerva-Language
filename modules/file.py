class cfile:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = "file"
    def open(self, path):
      self.value = open(path)
    def close(self):
      self.value.close()
    
def main(pline, names, digits, symbols, dsymbols, levels, linenum):
    namests = []
    aftersymbol = False
    inbracket = False
    path = ''
    operation = ''
    for i in pline[1:]:
      if i == '=':
        aftersymbol = not aftersymbol
      if i in ['(', ')']:
        inbracket = not inbracket
      elif aftersymbol == False:
        namests.append(i)
      elif inbracket:
        path = i[1:]
      else:
        operation = i
    
    if operation == 'open':
      for i in namests:
        
    return names, levels, linenum