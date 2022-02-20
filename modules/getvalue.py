def lexlist(i):
  invars = False
  name = ''
  num = ''
  for f in i:
    if f in "[]":
      invars = not invars
    elif invars:
      num = num + f
    elif invars == False:
      name = name + f
  return name, int(num)

def main(i, digits, names):
  if '.' in i:
    type = 'float'
    value = float(i)
  elif i[-1] in digits:
    type = 'int'
    value = int(i)
  elif i[0] == '#':
    type = 'str'
    value = i[1:]
  elif i in names:
    type = names[i].type
    value = names[i].value
  elif i in ['true','false']:
    type = 'bool'
    value = 'true' == i
  elif i in [True, False]:
    type = 'bool'
    value = i
  elif i[-1] == ']':
    name, num = lexlist(i)
    type, value = names[name].get(num, digits, names)
  else:
    type = 'Null'
    value = 'Null'
  return type, value
