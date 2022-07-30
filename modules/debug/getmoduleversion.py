import mtoken
version = "220730.1"
type = "tt_module"

def main(value, names, levels, position):
    for i in value:
        if i.type in ["tt_module"]: moduleversion = names[i.value].version
        else: print(f"EE {i.type}:{i.value} is not a module.")
    return mtoken.t('tt_char', moduleversion), names, levels, position
