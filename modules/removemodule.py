version = "2022.08.05.1"
type = 'tt_module'

def main(value, names, levels, position):
    a = 0
    while a < len(value):
        i = value[a]
        if i.type in ['tt_comma']: cheese = 0
        elif i.value in names and i.type == 'tt_module': names.pop(i.value)
        else: print(f'\033[33mWW module {i.value} cant be removed.')
        a += 1
    return 0, names, levels, position
