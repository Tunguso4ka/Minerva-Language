import modules.notforuse.getvalue as getvalue, random
version = "2022.08.07.1"
type = "tt_module"

class template:
    def __init__(self, name, value, do, startpos, currentpos):
        self.name = name
        self.value = value
        self.do = do
        self.startpos = startpos
        self.currentpos = currentpos
        self.type = 'switch'
    def level_end(self, names, levels, position):
        levels.pop()
        return names, levels, position

def main(values, names, levels, position):
    name = f'switch{str(position)}-{str(random.randint(0, 999))}'
    do = names[levels[-1]].do
    names[name] = template(name, getvalue.get(values[0], names), do, position, position)
    levels.append(name)
    return None, names, levels, position
