version = "2022.08.07.1"
type = "tt_module"

def get(t, names):
    match t.type:
        case ('tt_int'|'tt_float'|'tt_char'|'tt_bool'): return t.value
        case 'tt_unknown': return names[t.value].value
        case ('switch'): return t.value.value
        case 'tt_comma': return ' '
        case _: return 'None'
