import mtoken, modules.notforuse.getvalue
version = "2023.03.22.1"
type = "tt_module"

def main(values, names, levels, position):
    variables=[]
    symbol=' '
    if values[-1].value == ';': values.pop()
    for i in values:
        if i.value in ['=']: symbol = i
        elif symbol == ' ': variables.append(i)
    match symbol.type:
        case "tt_equal":
            for i in variables: names[i.value] = mtoken.t('tt_bool', bool(modules.notforuse.getvalue.get(values[-1], names)))
        case _: print(f'EE You cant use {symbol.type} with bool.')
    return 0, names, levels, position
