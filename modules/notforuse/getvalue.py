version = "2022.08.07.1"
type = "tt_module"
debug = False

def get(t, names):
    if debug:
        try: print("GETVALUE",t.type, t.value, names[t.value].value)
        except: print("GETVALUE",t.type, t.value)
    match t.type:
        case ('tt_int'|'tt_float'|'tt_char'|'tt_bool'): return t.value
        case 'tt_unknown': return names[t.value].value
        case ('switch'): return t.value
        case 'tt_comma': return ' '
        case _: return 'None'
