import mtoken
version = "220730.1"
type = "tt_module"

def main(value, names, levels, position):
    result = ''
    match value[0].value:
        case 'levels': result = levels
        case 'names': result = names
        case 'position': result = position
        case _: result = 'None'
    return mtoken.t('tt_char', result), names, levels, position
