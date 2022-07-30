import modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def main(values, names, levels, position):
    for i in values: position = int(modules.notforuse.getvalue.get(i, names))
    return None, names, levels, position - 1
