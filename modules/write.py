import modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def main(values, names, levels, position):
    result = ''
    for i in values: result += str(modules.notforuse.getvalue.get(i, names))
    print(result)
    return 0, names, levels, position
