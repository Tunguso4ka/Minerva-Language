from os.path import exists

version = "220730.1"
type = "tt_module"

def main(value, names, levels, position):
    a = 0
    while a < len(value):
        i = value[a]
        if i.type in ['tt_comma', 'tt_parenthes_open', 'tt_parenthes_close']: cheese = 0
        elif exists('modules/' + i.value.replace('.', '/') + ".py"): names[i.value] = __import__('modules.' + i.value, fromlist = ['.'])
        elif exists('modules/' + i.value.replace('.', '/') + '.minerva'): print(f'EE Module "{i.type}:{i.value}.minerva" wasn\'t loaded.')
        elif a+2 <= len(value) and value[a+1].type == 'tt_equal' and exists('modules/' + value[a+2].value.replace('.', '/') + '.py'): names[i.value] = __import__('modules.' + value[a+2].value, fromlist = ['.']); a+=2
        else: print(f'\033[33mWW Module "{i.type}:{i.value}" wasn\'t loaded because it doesnt exists.')
        a += 1
    return 0, names, levels, position
