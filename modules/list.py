import modules.getvalue

class clist:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = "list"
    def get(self, num, digits, names):
      return modules.getvalue.main(str(self.value[num]), digits, names)
    def add(self, var):
      self.value.append(var)
    def crop(self):
      self.value.pop()

def main(pline, names, digits, symbols, dsymbols, levels, linenum):
  equal_reached = False
  result = ''
  mode = ''
  namests = []
  vars = []
  for i in pline[1:]:
    if i in ['=', 'add', 'crop']:
      mode = i
      equal_reached = not equal_reached
    elif equal_reached == False:
      namests.append(i)
    elif mode in ['=', 'add'] and equal_reached == True:
      type, value = modules.getvalue.main(i, digits, names)
      vars.append(value)

  if mode == '=':
    for i in namests:
      names[i] = clist(i, vars)
  elif mode == 'add':
    for i in namests:
      for f in vars:
        names[i].add(f)
  elif mode == 'crop':
    for i in namests:
      names[i].crop()
  return names, levels, linenum
