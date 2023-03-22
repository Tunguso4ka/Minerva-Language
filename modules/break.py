version = "2022.08.10.1"
type = "tt_module"

def main(values, names, levels, position):
    if names[levels[-1]].type in ['if'] and names[levels[-2]].type in ['function', 'while', 'for']:
        names, levels, position = names[levels[-1]].level_end(names, levels, position)
    names, levels, position = names[levels[-1]].level_end(names, levels, position)
    return None, names, levels, position
