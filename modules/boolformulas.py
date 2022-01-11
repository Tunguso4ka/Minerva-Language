#a == a; a != a; a > a; a < a; a <= a; a >= a;
def main(formula):
    if formula[1] == '==':
        return formula[0] == formula[2]
    elif formula[1] == '!=':
        return formula[0] != formula[2]
    elif formula[1] == '>':
        return formula[0] > formula[2]
    elif formula[1] == '<':
        return formula[0] < formula[2]
    elif formula[1] == '<=':
        return formula[0] <= formula[2]
    elif formula[1] == '>=':
        return formula[0] >= formula[2]
    elif formula[1] == '&&':
        return formula[0] and formula[2]
    elif formula[1] == '||':
        return formula[0] or formula[2]
