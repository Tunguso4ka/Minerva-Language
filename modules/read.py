import mtoken, modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def main(values, names, levels, position):
    outtext = ''
    for i in values: outtext += str(modules.notforuse.getvalue.get(i, names))
    result = input(f'\033[93m{outtext}\033[0m')
    return mtoken.t('tt_char', result), names, levels, position
