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
  elif i in names or i in ['true','false']:
    type = names[i].type
    value = names[i].value
  elif i in [True, False]:
    type = 'bool'
  else:
    type = 'Null'
    value = 'Null'
  return type, value
