import modules.notforuse.mathoper, modules.notforuse.booloper
version = "220730.1"
type = "tt_module"

def main(formula, names, levels, position):
    while len(formula) > 1:
        math = True
        biggestoper = ' '
        bo_pos = -1
        f = 0
        for i in formula:
            if i.type in ['tt_int', 'tt_float', 'tt_bool', 'tt_char', 'tt_unknown']: skip = 0
            elif i.value[0] in '/*%':
                math = True
                biggestoper = i.value
                bo_pos = f
            elif i.value in '+-' and biggestoper in ['==', '>=', '>', '<=', '<', '!', '!=', '||', '&&', '>>', '<<', ' ']:
                math = True
                biggestoper = i.value
                bo_pos = f
            elif i.value in ['==', '>=', '>', '<=', '<', '!', '!=', '||', '&&'] and biggestoper[0] in " ":
                math = False
                biggestoper = i.value
                bo_pos = f
            f+=1
        if math:
            formula[bo_pos] = modules.notforuse.mathoper.solve(formula[bo_pos-1], formula[bo_pos], formula[bo_pos+1], names)
            formula.pop(bo_pos+1)
            formula.pop(bo_pos-1)
        else:
            formula[bo_pos] = modules.notforuse.booloper.solve(formula[bo_pos-1], formula[bo_pos], formula[bo_pos+1], names)
            formula.pop(bo_pos+1)
            formula.pop(bo_pos-1)
    return formula[0], names, levels, position


