import mtoken, modules.notforuse.getvalue
version = "2023.03.22.1"
type = "tt_module"

def main(values, names, levels, position):
    variables=[]
    symbol=' '
    if values[-1].value == ';': values.pop()
    for i in values:
        if i.value in ['=', '+=', '-=', '*=', '/=', '//=', '%=', '++', '--']: symbol = i
        elif symbol == ' ': variables.append(i)
    match symbol.type:
        case "tt_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_add_and_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) + int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_sub_and_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) - int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_mul_and_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) * int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_div_and_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) / int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_div_without_remaind_and_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) // int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_rem_and_equal":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) % int(modules.notforuse.getvalue.get(values[-1], names)))
        case "tt_increment":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) + 1)
        case "tt_decrement":
            for i in variables: names[i.value] = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(names[i.value], names)) - 1)
        case _: print(f'EE You cant use {symbol.type} with int.')
    return None, names, levels, position
