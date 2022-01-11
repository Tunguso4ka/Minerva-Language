def main(formula):
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