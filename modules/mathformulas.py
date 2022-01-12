def solveformula(formula):
  if formula[1] == '+':
    return formula[0] + formula[2]
  elif formula[1] == '-':
    return formula[0] - formula[2]
  elif formula[1] == '*':
    return formula[0] * formula[2]
  elif formula[1] == '/':
    return formula[0] / formula[2]
  elif formula[1] == '%':
    return formula[0] % formula[2]

def lex(formula):
  biggestsymbol = ''
  t = 0
  a = t
  for i in formula:
    if i in ['+', '-', '*', '/', '%']:
      if biggestsymbol in ['', '+', '-']:
        biggestsymbol = i
        a = t
      elif biggestsymbol == '':
        a = t
        biggestsymbol = i
    t += 1

  print(formula)
  formula[a] = solveformula([formula[a-1], formula[a], formula[a+1]])
  formula.pop(a+1)
  formula.pop(a-1)
  print(formula)
  return formula

def main(formula):
  while len(formula) > 1:
    print(len(formula))
    formula = lex(formula)
  return formula[0]

