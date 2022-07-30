from os.path import exists

version = "220730.1"
type = "tt_module"

def main(value, names, levels, position):
    for i in value:
        if i.type in ['tt_comma', 'tt_parenthes_open', 'tt_parenthes_close']: cheese = 0
        elif exists('modules/' + i.value.replace('.', '/') + ".py"): names[i.value] = __import__('modules.' + i.value, fromlist = [' '])
        elif exists('modules/' + i.value.replace('.', '/') + '.minerva'): print(f'EE Module "{i.type}:{i.value}.minerva" wasn\'t loaded.')
        else: print(f'EE Module "{i.type}:{i.value}" wasn\'t loaded because it doesnt exists.')
    return 0, names, levels, position
