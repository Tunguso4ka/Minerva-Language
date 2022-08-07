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
        self.type = "tt_module"
    def main(self, values, names, levels, position):
        levels.append(self.name)
        self.do = True
        position = self.startpos
        return None, names, levels, position
    def level_end(self, names, levels, position):
        levels.pop()
        if self.do: position = names[levels[-1]].currentpos + 1
        return names, levels, position

def main(values, names, levels, position):
    name = values[0].value
    names[name] = template(name, None, False, position, position)
    levels.append(name)
    return None, names, levels, position
