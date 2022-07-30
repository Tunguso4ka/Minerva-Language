import mtoken, modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def main(values, names, levels, position):
    variables=[]
    symbol=' '
    for i in values:
        if i.value in ['=', '+=', '-=', '*=', '/=', '//=', '%=']: symbol = i
        elif symbol == ' ': variables.append(i)
    match symbol.type:
        case "tt_equal": for i in variables: names[i.value] = mtoken.t('tt_char', str(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_add_and_equal": for i in variables: names[i.value] = mtoken.t('tt_char', str(modules.notforuse.getvalue.get(names[i.value], names)) + str(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_mul_and_equal": for i in variables: names[i.value] = mtoken.t('tt_char', str(modules.notforuse.getvalue.get(names[i.value], names)) * modules.notforuse.getvalue.get(values[-1], names))
        case _: print(f'EE You cant use {symbol.type} with char.')
    return 0, names, levels, position
