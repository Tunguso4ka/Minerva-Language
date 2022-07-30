from time import sleep as tsleep
import modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def main(values, names, levels, position):
    result = 0
    for i in values: result = float(modules.notforuse.getvalue.get(i, names))
    tsleep(result)
    return 0, names, levels, position
