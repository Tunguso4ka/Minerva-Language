import mtoken, modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def main(values, names, levels, position):
    type = ''
    for i in values:
        match i.type:
            case 'tt_converttype': type = i.value
            case ('tt_int'|'tt_float'|'tt_char'|'tt_bool'):
                match type:
                    case 'toint': result = mtoken.t('tt_int', int(modules.notforuse.getvalue.get(i, names)))
                    case 'tofloat': result = mtoken.t('tt_float', float(modules.notforuse.getvalue.get(i, names)))
                    case 'tobool': result = mtoken.t('tt_bool', bool(modules.notforuse.getvalue.get(i, names)))
                    case 'tochar': result = mtoken.t('tt_char', str(modules.notforuse.getvalue.get(i, names)))
    return result, names, levels, position
