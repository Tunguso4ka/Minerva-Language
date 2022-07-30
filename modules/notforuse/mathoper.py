import mtoken, modules.notforuse.getvalue
version = "220730.1"
type = "tt_module"

def solve(var0, symbol, var1, names):
    result = 0
    match symbol.value:
        case '+': result = modules.notforuse.getvalue.get(var0, names) + modules.notforuse.getvalue.get(var1, names)
        case '-': result = modules.notforuse.getvalue.get(var0, names) - modules.notforuse.getvalue.get(var1, names)
        case '*': result = modules.notforuse.getvalue.get(var0, names) * modules.notforuse.getvalue.get(var1, names)
        case '/': result = modules.notforuse.getvalue.get(var0, names) / modules.notforuse.getvalue.get(var1, names)
        case '//': result = modules.notforuse.getvalue.get(var0, names) // modules.notforuse.getvalue.get(var1, names)
        case '%': result = modules.notforuse.getvalue.get(var0, names) % modules.notforuse.getvalue.get(var1, names)
        case '++': result = modules.notforuse.getvalue.get(var0, names) + 1
        case '--': result = modules.notforuse.getvalue.get(var0, names) - 1
        case '>>': result = modules.notforuse.getvalue.get(var0, names) >> modules.notforuse.getvalue.get(var1, names)
        case '<<': result = modules.notforuse.getvalue.get(var0, names) << modules.notforuse.getvalue.get(var1, names)
    return mtoken.t(var0.type, result)
